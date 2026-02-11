# DB Schema: sky_agent_factory.db (draft)

-- Projects
CREATE TABLE projects (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  slug TEXT UNIQUE,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Target URLs to scrape
CREATE TABLE target_urls (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  project_id INTEGER REFERENCES projects(id),
  url TEXT NOT NULL,
  source TEXT,
  last_scraped DATETIME,
  status TEXT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Pages (scraped HTML / metadata)
CREATE TABLE pages (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  target_url_id INTEGER REFERENCES target_urls(id),
  url TEXT,
  title TEXT,
  html TEXT,
  extracted_md TEXT, -- converted markdown
  metadata JSON,
  snapshot_path TEXT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Artifacts (generated outputs)
CREATE TABLE artifacts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  page_id INTEGER REFERENCES pages(id),
  type TEXT, -- 'md','html','css','image'
  path TEXT,
  metadata JSON,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Images / external resources
CREATE TABLE images (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  page_id INTEGER REFERENCES pages(id),
  original_url TEXT,
  local_path TEXT,
  license TEXT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Runs / logs
CREATE TABLE runs (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  project_id INTEGER REFERENCES projects(id),
  name TEXT,
  params JSON,
  status TEXT,
  started_at DATETIME,
  finished_at DATETIME,
  result_summary TEXT
);
