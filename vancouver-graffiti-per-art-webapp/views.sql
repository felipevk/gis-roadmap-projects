-- must run from public schema

-- Drop views if they exist
DROP VIEW IF EXISTS get_graffiti_per_public_art CASCADE;
DROP VIEW IF EXISTS get_graffiti CASCADE;
DROP VIEW IF EXISTS get_public_art CASCADE;

-- View 1
CREATE VIEW get_graffiti_per_public_art AS (
    WITH graffiti_areas AS (
         SELECT a_1.name,
            count(*) AS graffiti
           FROM vancouver_areas a_1
             LEFT JOIN vancouver_graffiti b_1 ON st_contains(a_1.geom, b_1.geom)
          GROUP BY a_1.name
        ), art_areas AS (
         SELECT a_1.name,
            count(*) AS art
           FROM vancouver_areas a_1
             LEFT JOIN vancouver_public_art b_1 ON st_contains(a_1.geom, b_1.geom)
          GROUP BY a_1.name
        ), gpa AS (
         SELECT a_1.name,
            b_1.art,
            a_1.graffiti,
            trunc(a_1.graffiti::numeric / b_1.art::numeric) AS graffitiperart
           FROM graffiti_areas a_1
             JOIN art_areas b_1 ON a_1.name::text = b_1.name::text
        )
 SELECT b.id,
    b.name,
    a.art,
    a.graffiti,
    a.graffitiperart,
    st_asgeojson(b.geom)::json AS geometry,
    b.area_m2
   FROM gpa a
     LEFT JOIN vancouver_areas b ON a.name::text = b.name::text
);

-- View 2
CREATE VIEW get_graffiti AS (
    SELECT id, st_asgeojson(geom)::json AS geometry FROM vancouver_graffiti
);

-- View 3
CREATE VIEW get_public_art AS (
    SELECT 
        id, 
        st_asgeojson(geom)::json AS geometry, 
        title_of_work AS name,
        type,
        status
   FROM vancouver_public_art
);

GRANT SELECT ON TABLE public.get_graffiti_per_public_art TO flask_webapp_user;
GRANT SELECT ON TABLE public.get_graffiti TO flask_webapp_user;
GRANT SELECT ON TABLE public.get_public_art TO flask_webapp_user;