CREATE TABLE sites (
    id           SERIAL PRIMARY KEY,
    domain       VARCHAR(255),
    protocol     VARCHAR(10),
    secure       BOOLEAN
);

CREATE INDEX sites_domain_idx ON sites(domain);

CREATE TABLE documents (
    id           SERIAL PRIMARY KEY,
    site_id      INT REFERENCES sites(id) ON DELETE CASCADE,
    location     VARCHAR(255),
    content      TEXT,
    visited      TIMESTAMP DEFAULT now(),
    hash         VARCHAR(64)
);

CREATE INDEX documents_location_idx ON documents(location);
CREATE INDEX documents_hash_idx ON documents(hash);

CREATE TABLE links (
    source       INT REFERENCES documents(id) ON DELETE CASCADE,
    target       INT REFERENCES documents(id) ON DELETE CASCADE,
    mark         NUMERIC (5,2),
    PRIMARY KEY (source, target)
);
