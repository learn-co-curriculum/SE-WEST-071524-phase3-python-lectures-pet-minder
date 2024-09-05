CREATE TABLE "pets" (
  "id" int PRIMARY KEY,
  "name" text,
  "species" text,
  "owner_id" int
);

CREATE TABLE "jobs" (
  "id" int PRIMARY KEY,
  "pet_id" int,
  "handler_id" int,
  "request" text,
  "date" datetime,
  "fee" float
);

ALTER TABLE "jobs" ADD FOREIGN KEY ("pet_id") REFERENCES "pets" ("id");
