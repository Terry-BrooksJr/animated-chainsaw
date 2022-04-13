DROP TABLE IF EXISTS "PlatformUsers";
CREATE TABLE IF NOT EXISTS "PlatformUsers" (
    user_id smallint NOT NULL DEFAULT nextval('"PlatformUsers_user_id_seq"'::regclass),
    username VARCHAR(8)   NOT NULL,
    user_first_name VARCHAR(255)   NOT NULL,
    user_last_name VARCHAR(255)   NOT NULL,
    daycare_facility smallint NOT NULL,
    role VARCHAR(4)   NOT NULL,
    password_hash VARCHAR(32)  ,
    created_at timestamp with time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    last_modified_at timestamp with time zone,
    last_login timestamp without time zone ,
    CONSTRAINT "User ID" PRIMARY KEY (user_id)
)

INSERT INTO PlatformUsers VALUES
(NULL,'csennett0@telegraph.co.uk','Clayborn','Sennett','cZXrvPEN','34X6',NULL,NULL,'false','admin','7/18/2021'),
(NULL,'rlindell1@state.tx.us','Rube','Lindell','FaTaGUOUMQH3','24J7',NULL,NULL,'false','user','5/7/2021'),
(NULL,'rcheesworth2@eepurl.com','Randene','Cheesworth','XinQBB','07Q4',NULL,NULL,'false','admin','4/6/2022'),
(NULL,'ppenketh3@ask.com','Pollyanna','Penketh','WMdAw6Wi','10C6',NULL,NULL,'true','user','3/18/2022'),
(NULL,'vmobberley4@bbb.org','Vincenty','Mobberley','ew36bK6','03Z2',NULL,NULL,'false','admin','12/19/2021'),
(NULL,'aorum5@oracle.com','Adams','Orum','1uESCZ6O','49O7',NULL,NULL,'false','admin','10/17/2021'),
(NULL,'abrecknock6@meetup.com','Arch','Brecknock','3eHE4SoQjCN','74Q4',NULL,NULL,'true','admin','5/8/2021'),
(NULL,'jrochewell7@cornell.edu','Jule','Rochewell','rDCqXLp','37Z2',NULL,NULL,'true','user','8/1/2021'),
(NULL,'kspire8@slate.com','Kele','Spire','fd9dHZn','10F7',NULL,NULL,'false','user','6/3/2021'),
(NULL,'blambourne9@cbsnews.com','Barty','Lambourne','nfcsfg','78U8',NULL,'2021-09-16 15:51:24','false','user','4/29/2021'),
(NULL,'bespinosaa@bandcamp.com','Burch','Espinosa','BGDqwxvzdb','48W7',NULL,NULL,'true','admin','2/26/2022'),
(NULL,'dquanb@ft.com','Dori','Quan','EXfzpEwmoq','48W7',NULL,NULL,'true','user','3/30/2021'),
(NULL,'phurdc@hostgator.com','Paxon','Hurd','dtziVIAO','39V8',NULL,NULL,'false','admin','10/13/2021'),
(NULL,'fstillmand@prnewswire.com','Frederick','Stillman','Y7vDo1RbK','74T3',NULL,NULL,'false','user','10/2/2021'),
(NULL,'kshowere@amazon.co.jp','Karia','Shower','ciQI1boP','77K9',NULL,NULL,'true','admin','8/30/2021');