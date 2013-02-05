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

-- FROM SSJP

CREATE TABLE concepts (
    concept_id   INT PRIMARY KEY,
    word         VARCHAR(64) NOT NULL DEFAULT '',
    num          INT NOT NULL,
    etiquette    VARCHAR(30) NOT NULL DEFAULT '',
    lp_id 		 INT DEFAULT 0,
    sdesc        VARCHAR(100) NOT NULL DEFAULT '',
    mode         INT NOT NULL DEFAULT 0,
    aux          INT NOT NULL DEFAULT 0,
    
    UNIQUE (word, sdesc),
    UNIQUE (word, num),
    
    CHECK (num >= 0),
    CHECK (lp_id >= 0),
    CHECK (mode >= 0),
    CHECK (aux >= 0)
);

CREATE INDEX concepts_word_idx ON concepts(word);
CREATE INDEX concepts_sdesc_idx ON concepts(sdesc);
CREATE INDEX concepts_num_idx ON concepts(num);    

CREATE TABLE relation (
    concept_id   INT NOT NULL DEFAULT 0,
    r_concept_id INT NOT NULL DEFAULT 0,
    rel_id       INT NOT NULL DEFAULT 0,
    attr_l_num   INT NOT NULL DEFAULT 0,
    num          INT NOT NULL DEFAULT 0,
    aux          INT NOT NULL DEFAULT 0,
    category     INT NOT NULL DEFAULT 0,
    
    PRIMARY KEY(concept_id, r_concept_id, category)
);

CREATE INDEX relation_r_concept_idx ON relation(r_concept_id);

CREATE TABLE relation_name (
    rid          INT PRIMARY KEY,
    name         VARCHAR(255) NOT NULL
);

CREATE INDEX relation_name_name_idx ON relation_name(name);