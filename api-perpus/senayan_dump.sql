/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19  Distrib 10.11.13-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: perpus_dev
-- ------------------------------------------------------
-- Server version	10.11.13-MariaDB-0ubuntu0.24.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=253 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add backup log',7,'add_backuplog'),
(26,'Can change backup log',7,'change_backuplog'),
(27,'Can delete backup log',7,'delete_backuplog'),
(28,'Can view backup log',7,'view_backuplog'),
(29,'Can add biblio',8,'add_biblio'),
(30,'Can change biblio',8,'change_biblio'),
(31,'Can delete biblio',8,'delete_biblio'),
(32,'Can view biblio',8,'view_biblio'),
(33,'Can add biblio attachment',9,'add_biblioattachment'),
(34,'Can change biblio attachment',9,'change_biblioattachment'),
(35,'Can delete biblio attachment',9,'delete_biblioattachment'),
(36,'Can view biblio attachment',9,'view_biblioattachment'),
(37,'Can add biblio author',10,'add_biblioauthor'),
(38,'Can change biblio author',10,'change_biblioauthor'),
(39,'Can delete biblio author',10,'delete_biblioauthor'),
(40,'Can view biblio author',10,'view_biblioauthor'),
(41,'Can add biblio custom',11,'add_bibliocustom'),
(42,'Can change biblio custom',11,'change_bibliocustom'),
(43,'Can delete biblio custom',11,'delete_bibliocustom'),
(44,'Can view biblio custom',11,'view_bibliocustom'),
(45,'Can add biblio log',12,'add_bibliolog'),
(46,'Can change biblio log',12,'change_bibliolog'),
(47,'Can delete biblio log',12,'delete_bibliolog'),
(48,'Can view biblio log',12,'view_bibliolog'),
(49,'Can add biblio relation',13,'add_bibliorelation'),
(50,'Can change biblio relation',13,'change_bibliorelation'),
(51,'Can delete biblio relation',13,'delete_bibliorelation'),
(52,'Can view biblio relation',13,'view_bibliorelation'),
(53,'Can add biblio topic',14,'add_bibliotopic'),
(54,'Can change biblio topic',14,'change_bibliotopic'),
(55,'Can delete biblio topic',14,'delete_bibliotopic'),
(56,'Can view biblio topic',14,'view_bibliotopic'),
(57,'Can add content',15,'add_content'),
(58,'Can change content',15,'change_content'),
(59,'Can delete content',15,'delete_content'),
(60,'Can view content',15,'view_content'),
(61,'Can add files',16,'add_files'),
(62,'Can change files',16,'change_files'),
(63,'Can delete files',16,'delete_files'),
(64,'Can view files',16,'view_files'),
(65,'Can add files read',17,'add_filesread'),
(66,'Can change files read',17,'change_filesread'),
(67,'Can delete files read',17,'delete_filesread'),
(68,'Can view files read',17,'view_filesread'),
(69,'Can add fines',18,'add_fines'),
(70,'Can change fines',18,'change_fines'),
(71,'Can delete fines',18,'delete_fines'),
(72,'Can view fines',18,'view_fines'),
(73,'Can add holiday',19,'add_holiday'),
(74,'Can change holiday',19,'change_holiday'),
(75,'Can delete holiday',19,'delete_holiday'),
(76,'Can view holiday',19,'view_holiday'),
(77,'Can add index documents',20,'add_indexdocuments'),
(78,'Can change index documents',20,'change_indexdocuments'),
(79,'Can delete index documents',20,'delete_indexdocuments'),
(80,'Can view index documents',20,'view_indexdocuments'),
(81,'Can add index words',21,'add_indexwords'),
(82,'Can change index words',21,'change_indexwords'),
(83,'Can delete index words',21,'delete_indexwords'),
(84,'Can view index words',21,'view_indexwords'),
(85,'Can add item',22,'add_item'),
(86,'Can change item',22,'change_item'),
(87,'Can delete item',22,'delete_item'),
(88,'Can view item',22,'view_item'),
(89,'Can add kardex',23,'add_kardex'),
(90,'Can change kardex',23,'change_kardex'),
(91,'Can delete kardex',23,'delete_kardex'),
(92,'Can view kardex',23,'view_kardex'),
(93,'Can add loan',24,'add_loan'),
(94,'Can change loan',24,'change_loan'),
(95,'Can delete loan',24,'delete_loan'),
(96,'Can view loan',24,'view_loan'),
(97,'Can add loan history',25,'add_loanhistory'),
(98,'Can change loan history',25,'change_loanhistory'),
(99,'Can delete loan history',25,'delete_loanhistory'),
(100,'Can view loan history',25,'view_loanhistory'),
(101,'Can add mst author',26,'add_mstauthor'),
(102,'Can change mst author',26,'change_mstauthor'),
(103,'Can delete mst author',26,'delete_mstauthor'),
(104,'Can view mst author',26,'view_mstauthor'),
(105,'Can add mst carrier type',27,'add_mstcarriertype'),
(106,'Can change mst carrier type',27,'change_mstcarriertype'),
(107,'Can delete mst carrier type',27,'delete_mstcarriertype'),
(108,'Can view mst carrier type',27,'view_mstcarriertype'),
(109,'Can add mst coll type',28,'add_mstcolltype'),
(110,'Can change mst coll type',28,'change_mstcolltype'),
(111,'Can delete mst coll type',28,'delete_mstcolltype'),
(112,'Can view mst coll type',28,'view_mstcolltype'),
(113,'Can add mst content type',29,'add_mstcontenttype'),
(114,'Can change mst content type',29,'change_mstcontenttype'),
(115,'Can delete mst content type',29,'delete_mstcontenttype'),
(116,'Can view mst content type',29,'view_mstcontenttype'),
(117,'Can add mst custom field',30,'add_mstcustomfield'),
(118,'Can change mst custom field',30,'change_mstcustomfield'),
(119,'Can delete mst custom field',30,'delete_mstcustomfield'),
(120,'Can view mst custom field',30,'view_mstcustomfield'),
(121,'Can add mst frequency',31,'add_mstfrequency'),
(122,'Can change mst frequency',31,'change_mstfrequency'),
(123,'Can delete mst frequency',31,'delete_mstfrequency'),
(124,'Can view mst frequency',31,'view_mstfrequency'),
(125,'Can add mst gmd',32,'add_mstgmd'),
(126,'Can change mst gmd',32,'change_mstgmd'),
(127,'Can delete mst gmd',32,'delete_mstgmd'),
(128,'Can view mst gmd',32,'view_mstgmd'),
(129,'Can add mst item status',33,'add_mstitemstatus'),
(130,'Can change mst item status',33,'change_mstitemstatus'),
(131,'Can delete mst item status',33,'delete_mstitemstatus'),
(132,'Can view mst item status',33,'view_mstitemstatus'),
(133,'Can add mst label',34,'add_mstlabel'),
(134,'Can change mst label',34,'change_mstlabel'),
(135,'Can delete mst label',34,'delete_mstlabel'),
(136,'Can view mst label',34,'view_mstlabel'),
(137,'Can add mst language',35,'add_mstlanguage'),
(138,'Can change mst language',35,'change_mstlanguage'),
(139,'Can delete mst language',35,'delete_mstlanguage'),
(140,'Can view mst language',35,'view_mstlanguage'),
(141,'Can add mst loan rules',36,'add_mstloanrules'),
(142,'Can change mst loan rules',36,'change_mstloanrules'),
(143,'Can delete mst loan rules',36,'delete_mstloanrules'),
(144,'Can view mst loan rules',36,'view_mstloanrules'),
(145,'Can add mst location',37,'add_mstlocation'),
(146,'Can change mst location',37,'change_mstlocation'),
(147,'Can delete mst location',37,'delete_mstlocation'),
(148,'Can view mst location',37,'view_mstlocation'),
(149,'Can add mst media type',38,'add_mstmediatype'),
(150,'Can change mst media type',38,'change_mstmediatype'),
(151,'Can delete mst media type',38,'delete_mstmediatype'),
(152,'Can view mst media type',38,'view_mstmediatype'),
(153,'Can add mst module',39,'add_mstmodule'),
(154,'Can change mst module',39,'change_mstmodule'),
(155,'Can delete mst module',39,'delete_mstmodule'),
(156,'Can view mst module',39,'view_mstmodule'),
(157,'Can add mst place',40,'add_mstplace'),
(158,'Can change mst place',40,'change_mstplace'),
(159,'Can delete mst place',40,'delete_mstplace'),
(160,'Can view mst place',40,'view_mstplace'),
(161,'Can add mst publisher',41,'add_mstpublisher'),
(162,'Can change mst publisher',41,'change_mstpublisher'),
(163,'Can delete mst publisher',41,'delete_mstpublisher'),
(164,'Can view mst publisher',41,'view_mstpublisher'),
(165,'Can add mst relation term',42,'add_mstrelationterm'),
(166,'Can change mst relation term',42,'change_mstrelationterm'),
(167,'Can delete mst relation term',42,'delete_mstrelationterm'),
(168,'Can view mst relation term',42,'view_mstrelationterm'),
(169,'Can add mst servers',43,'add_mstservers'),
(170,'Can change mst servers',43,'change_mstservers'),
(171,'Can delete mst servers',43,'delete_mstservers'),
(172,'Can view mst servers',43,'view_mstservers'),
(173,'Can add mst supplier',44,'add_mstsupplier'),
(174,'Can change mst supplier',44,'change_mstsupplier'),
(175,'Can delete mst supplier',44,'delete_mstsupplier'),
(176,'Can view mst supplier',44,'view_mstsupplier'),
(177,'Can add mst topic',45,'add_msttopic'),
(178,'Can change mst topic',45,'change_msttopic'),
(179,'Can delete mst topic',45,'delete_msttopic'),
(180,'Can view mst topic',45,'view_msttopic'),
(181,'Can add mst voc ctrl',46,'add_mstvocctrl'),
(182,'Can change mst voc ctrl',46,'change_mstvocctrl'),
(183,'Can delete mst voc ctrl',46,'delete_mstvocctrl'),
(184,'Can view mst voc ctrl',46,'view_mstvocctrl'),
(185,'Can add plugins',47,'add_plugins'),
(186,'Can change plugins',47,'change_plugins'),
(187,'Can delete plugins',47,'delete_plugins'),
(188,'Can view plugins',47,'view_plugins'),
(189,'Can add reserve',48,'add_reserve'),
(190,'Can change reserve',48,'change_reserve'),
(191,'Can delete reserve',48,'delete_reserve'),
(192,'Can view reserve',48,'view_reserve'),
(193,'Can add search biblio',49,'add_searchbiblio'),
(194,'Can change search biblio',49,'change_searchbiblio'),
(195,'Can delete search biblio',49,'delete_searchbiblio'),
(196,'Can view search biblio',49,'view_searchbiblio'),
(197,'Can add serial',50,'add_serial'),
(198,'Can change serial',50,'change_serial'),
(199,'Can delete serial',50,'delete_serial'),
(200,'Can view serial',50,'view_serial'),
(201,'Can add setting',51,'add_setting'),
(202,'Can change setting',51,'change_setting'),
(203,'Can delete setting',51,'delete_setting'),
(204,'Can view setting',51,'view_setting'),
(205,'Can add stock take',52,'add_stocktake'),
(206,'Can change stock take',52,'change_stocktake'),
(207,'Can delete stock take',52,'delete_stocktake'),
(208,'Can view stock take',52,'view_stocktake'),
(209,'Can add stock take item',53,'add_stocktakeitem'),
(210,'Can change stock take item',53,'change_stocktakeitem'),
(211,'Can delete stock take item',53,'delete_stocktakeitem'),
(212,'Can view stock take item',53,'view_stocktakeitem'),
(213,'Can add group access',54,'add_groupaccess'),
(214,'Can change group access',54,'change_groupaccess'),
(215,'Can delete group access',54,'delete_groupaccess'),
(216,'Can view group access',54,'view_groupaccess'),
(217,'Can add system log',55,'add_systemlog'),
(218,'Can change system log',55,'change_systemlog'),
(219,'Can delete system log',55,'delete_systemlog'),
(220,'Can view system log',55,'view_systemlog'),
(221,'Can add user',56,'add_user'),
(222,'Can change user',56,'change_user'),
(223,'Can delete user',56,'delete_user'),
(224,'Can view user',56,'view_user'),
(225,'Can add user group',57,'add_usergroup'),
(226,'Can change user group',57,'change_usergroup'),
(227,'Can delete user group',57,'delete_usergroup'),
(228,'Can view user group',57,'view_usergroup'),
(229,'Can add email verification',58,'add_emailverification'),
(230,'Can change email verification',58,'change_emailverification'),
(231,'Can delete email verification',58,'delete_emailverification'),
(232,'Can view email verification',58,'view_emailverification'),
(233,'Can add comment',59,'add_comment'),
(234,'Can change comment',59,'change_comment'),
(235,'Can delete comment',59,'delete_comment'),
(236,'Can view comment',59,'view_comment'),
(237,'Can add member',60,'add_member'),
(238,'Can change member',60,'change_member'),
(239,'Can delete member',60,'delete_member'),
(240,'Can view member',60,'view_member'),
(241,'Can add member custom',61,'add_membercustom'),
(242,'Can change member custom',61,'change_membercustom'),
(243,'Can delete member custom',61,'delete_membercustom'),
(244,'Can view member custom',61,'view_membercustom'),
(245,'Can add mst member type',62,'add_mstmembertype'),
(246,'Can change mst member type',62,'change_mstmembertype'),
(247,'Can delete mst member type',62,'delete_mstmembertype'),
(248,'Can view mst member type',62,'view_mstmembertype'),
(249,'Can add visitor count',63,'add_visitorcount'),
(250,'Can change visitor count',63,'change_visitorcount'),
(251,'Can delete visitor count',63,'delete_visitorcount'),
(252,'Can view visitor count',63,'view_visitorcount');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backup_log`
--

DROP TABLE IF EXISTS `backup_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `backup_log` (
  `backup_log_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `backup_time` datetime(6) NOT NULL,
  `backup_file` longtext DEFAULT NULL,
  PRIMARY KEY (`backup_log_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backup_log`
--

LOCK TABLES `backup_log` WRITE;
/*!40000 ALTER TABLE `backup_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `backup_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `biblio`
--

DROP TABLE IF EXISTS `biblio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `biblio` (
  `biblio_id` int(11) NOT NULL AUTO_INCREMENT,
  `gmd_id` int(11) DEFAULT NULL,
  `title` longtext NOT NULL,
  `sor` varchar(200) DEFAULT NULL,
  `edition` varchar(50) DEFAULT NULL,
  `isbn_issn` varchar(32) DEFAULT NULL,
  `publisher_id` int(11) DEFAULT NULL,
  `publish_year` varchar(20) DEFAULT NULL,
  `collation` varchar(50) DEFAULT NULL,
  `series_title` varchar(200) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `language_id` varchar(5) NOT NULL,
  `source` varchar(3) DEFAULT NULL,
  `publish_place_id` int(11) DEFAULT NULL,
  `classification` varchar(40) DEFAULT NULL,
  `notes` longtext DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `file_att` varchar(255) DEFAULT NULL,
  `opac_hide` smallint(6) NOT NULL,
  `promoted` smallint(6) NOT NULL,
  `labels` longtext DEFAULT NULL,
  `frequency_id` int(11) NOT NULL,
  `spec_detail_info` longtext DEFAULT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `media_type_id` int(11) DEFAULT NULL,
  `carrier_type_id` int(11) DEFAULT NULL,
  `input_date` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  PRIMARY KEY (`biblio_id`),
  KEY `biblio_gmd_id_994f83_idx` (`gmd_id`,`publisher_id`,`language_id`,`publish_place_id`),
  KEY `biblio_classif_b35387_idx` (`classification`),
  KEY `biblio_opac_hi_9955fa_idx` (`opac_hide`,`promoted`),
  KEY `biblio_content_407203_idx` (`content_type_id`,`media_type_id`,`carrier_type_id`),
  KEY `biblio_uid_d6f88d_idx` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `biblio`
--

LOCK TABLES `biblio` WRITE;
/*!40000 ALTER TABLE `biblio` DISABLE KEYS */;
INSERT INTO `biblio` VALUES
(1,1,'Sample Book Title',NULL,NULL,NULL,1,'2023',NULL,NULL,NULL,'en',NULL,NULL,NULL,NULL,NULL,NULL,0,0,NULL,0,NULL,NULL,NULL,NULL,'2025-12-13 04:21:08.148009','2025-12-13 04:21:08.148017',NULL);
/*!40000 ALTER TABLE `biblio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `biblio_attachment`
--

DROP TABLE IF EXISTS `biblio_attachment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `biblio_attachment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `biblio_id` int(11) NOT NULL,
  `file_id` int(11) NOT NULL,
  `placement` varchar(20) DEFAULT NULL,
  `access_type` varchar(10) NOT NULL,
  `access_limit` longtext DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `biblio_atta_biblio__72d508_idx` (`biblio_id`),
  KEY `biblio_atta_file_id_a8384c_idx` (`file_id`),
  KEY `biblio_atta_biblio__438a63_idx` (`biblio_id`,`file_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `biblio_attachment`
--

LOCK TABLES `biblio_attachment` WRITE;
/*!40000 ALTER TABLE `biblio_attachment` DISABLE KEYS */;
/*!40000 ALTER TABLE `biblio_attachment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `biblio_author`
--

DROP TABLE IF EXISTS `biblio_author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `biblio_author` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `biblio_id` int(11) NOT NULL,
  `author_id` int(11) NOT NULL,
  `level` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `biblio_author_biblio_id_author_id_ef88ff51_uniq` (`biblio_id`,`author_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `biblio_author`
--

LOCK TABLES `biblio_author` WRITE;
/*!40000 ALTER TABLE `biblio_author` DISABLE KEYS */;
/*!40000 ALTER TABLE `biblio_author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `biblio_custom`
--

DROP TABLE IF EXISTS `biblio_custom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `biblio_custom` (
  `biblio_id` int(11) NOT NULL,
  PRIMARY KEY (`biblio_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `biblio_custom`
--

LOCK TABLES `biblio_custom` WRITE;
/*!40000 ALTER TABLE `biblio_custom` DISABLE KEYS */;
/*!40000 ALTER TABLE `biblio_custom` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `biblio_log`
--

DROP TABLE IF EXISTS `biblio_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `biblio_log` (
  `biblio_log_id` int(11) NOT NULL AUTO_INCREMENT,
  `biblio_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `realname` varchar(100) NOT NULL,
  `title` longtext NOT NULL,
  `ip` varchar(200) NOT NULL,
  `action` varchar(50) NOT NULL,
  `affectedrow` varchar(50) NOT NULL,
  `rawdata` longtext NOT NULL,
  `additional_information` longtext NOT NULL,
  `date` datetime(6) NOT NULL,
  PRIMARY KEY (`biblio_log_id`),
  KEY `biblio_log_realnam_56e9c8_idx` (`realname`),
  KEY `biblio_log_biblio__91285e_idx` (`biblio_id`),
  KEY `biblio_log_user_id_8594e6_idx` (`user_id`),
  KEY `biblio_log_ip_9f84b6_idx` (`ip`),
  KEY `biblio_log_action_a0f77e_idx` (`action`),
  KEY `biblio_log_affecte_269e42_idx` (`affectedrow`),
  KEY `biblio_log_date_031c5e_idx` (`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `biblio_log`
--

LOCK TABLES `biblio_log` WRITE;
/*!40000 ALTER TABLE `biblio_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `biblio_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `biblio_relation`
--

DROP TABLE IF EXISTS `biblio_relation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `biblio_relation` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `biblio_id` int(11) NOT NULL,
  `rel_biblio_id` int(11) NOT NULL,
  `rel_type` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `biblio_relation_biblio_id_rel_biblio_id_375dc54f_uniq` (`biblio_id`,`rel_biblio_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `biblio_relation`
--

LOCK TABLES `biblio_relation` WRITE;
/*!40000 ALTER TABLE `biblio_relation` DISABLE KEYS */;
/*!40000 ALTER TABLE `biblio_relation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `biblio_topic`
--

DROP TABLE IF EXISTS `biblio_topic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `biblio_topic` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `biblio_id` int(11) NOT NULL,
  `topic_id` int(11) NOT NULL,
  `level` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `biblio_topic_biblio_id_topic_id_b3a59b82_uniq` (`biblio_id`,`topic_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `biblio_topic`
--

LOCK TABLES `biblio_topic` WRITE;
/*!40000 ALTER TABLE `biblio_topic` DISABLE KEYS */;
/*!40000 ALTER TABLE `biblio_topic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `comment` (
  `comment_id` int(11) NOT NULL AUTO_INCREMENT,
  `biblio_id` int(11) NOT NULL,
  `member_id` varchar(20) NOT NULL,
  `comment` longtext NOT NULL,
  `input_date` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`comment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `content`
--

DROP TABLE IF EXISTS `content`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `content` (
  `content_id` int(11) NOT NULL AUTO_INCREMENT,
  `content_title` varchar(255) NOT NULL,
  `content_desc` longtext NOT NULL,
  `content_path` varchar(20) NOT NULL,
  `is_news` smallint(6) DEFAULT NULL,
  `input_date` datetime(6) NOT NULL,
  `last_update` datetime(6) NOT NULL,
  `content_ownpage` varchar(1) NOT NULL,
  PRIMARY KEY (`content_id`),
  UNIQUE KEY `content_path` (`content_path`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `content`
--

LOCK TABLES `content` WRITE;
/*!40000 ALTER TABLE `content` DISABLE KEYS */;
/*!40000 ALTER TABLE `content` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES
(1,'admin','logentry'),
(7,'api','backuplog'),
(8,'api','biblio'),
(9,'api','biblioattachment'),
(10,'api','biblioauthor'),
(11,'api','bibliocustom'),
(12,'api','bibliolog'),
(13,'api','bibliorelation'),
(14,'api','bibliotopic'),
(15,'api','content'),
(16,'api','files'),
(17,'api','filesread'),
(18,'api','fines'),
(19,'api','holiday'),
(20,'api','indexdocuments'),
(21,'api','indexwords'),
(22,'api','item'),
(23,'api','kardex'),
(24,'api','loan'),
(25,'api','loanhistory'),
(26,'api','mstauthor'),
(27,'api','mstcarriertype'),
(28,'api','mstcolltype'),
(29,'api','mstcontenttype'),
(30,'api','mstcustomfield'),
(31,'api','mstfrequency'),
(32,'api','mstgmd'),
(33,'api','mstitemstatus'),
(34,'api','mstlabel'),
(35,'api','mstlanguage'),
(36,'api','mstloanrules'),
(37,'api','mstlocation'),
(38,'api','mstmediatype'),
(39,'api','mstmodule'),
(40,'api','mstplace'),
(41,'api','mstpublisher'),
(42,'api','mstrelationterm'),
(43,'api','mstservers'),
(44,'api','mstsupplier'),
(45,'api','msttopic'),
(46,'api','mstvocctrl'),
(47,'api','plugins'),
(48,'api','reserve'),
(49,'api','searchbiblio'),
(50,'api','serial'),
(51,'api','setting'),
(52,'api','stocktake'),
(53,'api','stocktakeitem'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(58,'authentication','emailverification'),
(54,'authentication','groupaccess'),
(55,'authentication','systemlog'),
(56,'authentication','user'),
(57,'authentication','usergroup'),
(5,'contenttypes','contenttype'),
(6,'sessions','session'),
(59,'user','comment'),
(60,'user','member'),
(61,'user','membercustom'),
(62,'user','mstmembertype'),
(63,'user','visitorcount');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES
(1,'contenttypes','0001_initial','2025-09-17 03:54:39.785589'),
(2,'auth','0001_initial','2025-09-17 03:54:40.414796'),
(3,'admin','0001_initial','2025-09-17 03:54:40.534761'),
(4,'admin','0002_logentry_remove_auto_add','2025-09-17 03:54:40.545201'),
(5,'admin','0003_logentry_add_action_flag_choices','2025-09-17 03:54:40.554164'),
(6,'api','0001_initial','2025-09-17 03:54:43.654542'),
(7,'contenttypes','0002_remove_content_type_name','2025-09-17 03:54:43.772149'),
(8,'auth','0002_alter_permission_name_max_length','2025-09-17 03:54:43.823574'),
(9,'auth','0003_alter_user_email_max_length','2025-09-17 03:54:43.859476'),
(10,'auth','0004_alter_user_username_opts','2025-09-17 03:54:43.873441'),
(11,'auth','0005_alter_user_last_login_null','2025-09-17 03:54:43.922337'),
(12,'auth','0006_require_contenttypes_0002','2025-09-17 03:54:43.926636'),
(13,'auth','0007_alter_validators_add_error_messages','2025-09-17 03:54:43.942332'),
(14,'auth','0008_alter_user_username_max_length','2025-09-17 03:54:43.984989'),
(15,'auth','0009_alter_user_last_name_max_length','2025-09-17 03:54:44.024073'),
(16,'auth','0010_alter_group_name_max_length','2025-09-17 03:54:44.061634'),
(17,'auth','0011_update_proxy_permissions','2025-09-17 03:54:44.098429'),
(18,'auth','0012_alter_user_first_name_max_length','2025-09-17 03:54:44.166386'),
(19,'authentication','0001_initial','2025-09-17 03:54:44.415848'),
(20,'authentication','0002_emailverification','2025-09-17 03:54:44.449090'),
(21,'sessions','0001_initial','2025-09-17 03:54:44.505032'),
(22,'user','0001_initial','2025-09-17 03:54:44.775426'),
(23,'user','0002_auto_20250916_0332','2025-09-17 03:54:44.840663'),
(24,'user','0003_fix_password_field_length','2025-09-17 05:10:44.236858'),
(25,'user','0004_fix_password_field_length','2025-09-17 05:12:18.611421');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `email_verification`
--

DROP TABLE IF EXISTS `email_verification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `email_verification` (
  `verification_id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `token` varchar(100) NOT NULL,
  `member_id` varchar(20) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `expires_at` datetime(6) NOT NULL,
  `is_used` tinyint(1) NOT NULL,
  PRIMARY KEY (`verification_id`),
  UNIQUE KEY `token` (`token`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `email_verification`
--

LOCK TABLES `email_verification` WRITE;
/*!40000 ALTER TABLE `email_verification` DISABLE KEYS */;
INSERT INTO `email_verification` VALUES
(1,'john.doe@example.com','873406','1234567890123456','2025-09-17 05:12:37.651727','2025-09-18 05:12:37.651111',0),
(2,'danibaret014@gmail.com','785623','12121212212121212','2025-09-18 04:20:13.814376','2025-09-19 04:20:13.814161',0),
(3,'sajakcodingan@example.com','911244','3528012345678910','2025-09-18 04:39:13.178411','2025-09-19 04:39:13.177791',1),
(4,'user@example.com','907573','string','2025-09-22 03:39:43.738985','2025-09-23 03:39:43.738492',0);
/*!40000 ALTER TABLE `email_verification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `files`
--

DROP TABLE IF EXISTS `files`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `files` (
  `file_id` int(11) NOT NULL AUTO_INCREMENT,
  `file_title` longtext NOT NULL,
  `file_name` longtext NOT NULL,
  `file_url` longtext DEFAULT NULL,
  `file_dir` longtext DEFAULT NULL,
  `mime_type` varchar(100) DEFAULT NULL,
  `file_desc` longtext DEFAULT NULL,
  `file_key` longtext DEFAULT NULL,
  `uploader_id` int(11) NOT NULL,
  `input_date` datetime(6) NOT NULL,
  `last_update` datetime(6) NOT NULL,
  PRIMARY KEY (`file_id`),
  KEY `files_file_na_85b89e_idx` (`file_name`(768)),
  KEY `files_file_di_3392bc_idx` (`file_dir`(768))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `files`
--

LOCK TABLES `files` WRITE;
/*!40000 ALTER TABLE `files` DISABLE KEYS */;
/*!40000 ALTER TABLE `files` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `files_read`
--

DROP TABLE IF EXISTS `files_read`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `files_read` (
  `filelog_id` int(11) NOT NULL AUTO_INCREMENT,
  `file_id` int(11) NOT NULL,
  `date_read` datetime(6) NOT NULL,
  `member_id` varchar(20) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `client_ip` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`filelog_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `files_read`
--

LOCK TABLES `files_read` WRITE;
/*!40000 ALTER TABLE `files_read` DISABLE KEYS */;
/*!40000 ALTER TABLE `files_read` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fines`
--

DROP TABLE IF EXISTS `fines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `fines` (
  `fines_id` int(11) NOT NULL AUTO_INCREMENT,
  `fines_date` date NOT NULL,
  `member_id` varchar(20) NOT NULL,
  `debet` int(11) NOT NULL,
  `credit` int(11) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`fines_id`),
  KEY `fines_member__71f3b0_idx` (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fines`
--

LOCK TABLES `fines` WRITE;
/*!40000 ALTER TABLE `fines` DISABLE KEYS */;
/*!40000 ALTER TABLE `fines` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `group_access`
--

DROP TABLE IF EXISTS `group_access`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `group_access` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `module_id` int(11) NOT NULL,
  `menus` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`menus`)),
  `r` int(11) NOT NULL,
  `w` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_access_group_id_module_id_c4c0942c_uniq` (`group_id`,`module_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `group_access`
--

LOCK TABLES `group_access` WRITE;
/*!40000 ALTER TABLE `group_access` DISABLE KEYS */;
/*!40000 ALTER TABLE `group_access` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `holiday`
--

DROP TABLE IF EXISTS `holiday`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `holiday` (
  `holiday_id` int(11) NOT NULL AUTO_INCREMENT,
  `holiday_dayname` varchar(20) NOT NULL,
  `holiday_date` date DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`holiday_id`),
  UNIQUE KEY `holiday_holiday_dayname_holiday_date_3c632ebd_uniq` (`holiday_dayname`,`holiday_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `holiday`
--

LOCK TABLES `holiday` WRITE;
/*!40000 ALTER TABLE `holiday` DISABLE KEYS */;
/*!40000 ALTER TABLE `holiday` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_documents`
--

DROP TABLE IF EXISTS `index_documents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `index_documents` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `document_id` int(11) NOT NULL,
  `word_id` bigint(20) NOT NULL,
  `location` varchar(50) NOT NULL,
  `hit_count` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_documents_document_id_word_id_location_978badba_uniq` (`document_id`,`word_id`,`location`),
  KEY `index_docum_documen_a8955f_idx` (`document_id`),
  KEY `index_docum_word_id_11ddb2_idx` (`word_id`),
  KEY `index_docum_locatio_ba039a_idx` (`location`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_documents`
--

LOCK TABLES `index_documents` WRITE;
/*!40000 ALTER TABLE `index_documents` DISABLE KEYS */;
/*!40000 ALTER TABLE `index_documents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `index_words`
--

DROP TABLE IF EXISTS `index_words`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `index_words` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `word` varchar(50) NOT NULL,
  `num_hits` int(11) NOT NULL,
  `doc_hits` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `index_words`
--

LOCK TABLES `index_words` WRITE;
/*!40000 ALTER TABLE `index_words` DISABLE KEYS */;
/*!40000 ALTER TABLE `index_words` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `item` (
  `item_id` int(11) NOT NULL AUTO_INCREMENT,
  `biblio_id` int(11) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `coll_type_id` int(11) DEFAULT NULL,
  `item_code` varchar(20) DEFAULT NULL,
  `inventory_code` varchar(200) DEFAULT NULL,
  `received_date` date DEFAULT NULL,
  `supplier_id` varchar(6) DEFAULT NULL,
  `order_no` varchar(20) DEFAULT NULL,
  `location_id` varchar(3) DEFAULT NULL,
  `order_date` date DEFAULT NULL,
  `item_status_id` varchar(3) DEFAULT NULL,
  `site` varchar(50) DEFAULT NULL,
  `source` int(11) NOT NULL,
  `invoice` varchar(20) DEFAULT NULL,
  `price` int(11) DEFAULT NULL,
  `price_currency` varchar(10) DEFAULT NULL,
  `invoice_date` date DEFAULT NULL,
  `input_date` datetime(6) NOT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  PRIMARY KEY (`item_id`),
  UNIQUE KEY `item_code` (`item_code`),
  KEY `item_uid_643e49_idx` (`uid`),
  KEY `item_coll_ty_347499_idx` (`coll_type_id`,`location_id`,`item_status_id`),
  KEY `item_biblio__98cccc_idx` (`biblio_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item`
--

LOCK TABLES `item` WRITE;
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
/*!40000 ALTER TABLE `item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kardex`
--

DROP TABLE IF EXISTS `kardex`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `kardex` (
  `kardex_id` int(11) NOT NULL AUTO_INCREMENT,
  `date_expected` date NOT NULL,
  `date_received` date DEFAULT NULL,
  `seq_number` varchar(25) DEFAULT NULL,
  `notes` longtext DEFAULT NULL,
  `serial_id` int(11) DEFAULT NULL,
  `input_date` date NOT NULL,
  `last_update` date NOT NULL,
  PRIMARY KEY (`kardex_id`),
  KEY `kardex_serial__894732_idx` (`serial_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kardex`
--

LOCK TABLES `kardex` WRITE;
/*!40000 ALTER TABLE `kardex` DISABLE KEYS */;
/*!40000 ALTER TABLE `kardex` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loan`
--

DROP TABLE IF EXISTS `loan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `loan` (
  `loan_id` int(11) NOT NULL AUTO_INCREMENT,
  `item_code` varchar(20) DEFAULT NULL,
  `member_id` varchar(20) DEFAULT NULL,
  `loan_date` date NOT NULL,
  `due_date` date NOT NULL,
  `renewed` int(11) NOT NULL,
  `loan_rules_id` int(11) NOT NULL,
  `actual` date DEFAULT NULL,
  `is_lent` int(11) NOT NULL,
  `is_return` int(11) NOT NULL,
  `return_date` date DEFAULT NULL,
  `input_date` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  `uid` int(11) DEFAULT NULL,
  PRIMARY KEY (`loan_id`),
  KEY `loan_item_co_98665e_idx` (`item_code`),
  KEY `loan_member__9d2306_idx` (`member_id`),
  KEY `loan_input_d_ff9442_idx` (`input_date`,`last_update`,`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loan`
--

LOCK TABLES `loan` WRITE;
/*!40000 ALTER TABLE `loan` DISABLE KEYS */;
INSERT INTO `loan` VALUES
(1,'BK45781','1234567890123456','2025-09-17','2025-09-24',2147483647,2147483647,'2025-09-17',2147483647,2147483647,'2025-09-17',NULL,NULL,2147483647);
/*!40000 ALTER TABLE `loan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loan_history`
--

DROP TABLE IF EXISTS `loan_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `loan_history` (
  `loan_id` int(11) NOT NULL,
  `item_code` varchar(20) DEFAULT NULL,
  `biblio_id` int(11) NOT NULL,
  `title` varchar(300) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `classification` varchar(40) DEFAULT NULL,
  `gmd_name` varchar(30) DEFAULT NULL,
  `language_name` varchar(20) DEFAULT NULL,
  `location_name` varchar(100) DEFAULT NULL,
  `collection_type_name` varchar(100) DEFAULT NULL,
  `member_id` varchar(20) DEFAULT NULL,
  `member_name` varchar(100) DEFAULT NULL,
  `member_type_name` varchar(64) DEFAULT NULL,
  `loan_date` date DEFAULT NULL,
  `due_date` date DEFAULT NULL,
  `renewed` int(11) NOT NULL,
  `is_lent` int(11) NOT NULL,
  `is_return` int(11) NOT NULL,
  `return_date` date DEFAULT NULL,
  `input_date` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`loan_id`),
  KEY `loan_histor_member__7a8074_idx` (`member_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loan_history`
--

LOCK TABLES `loan_history` WRITE;
/*!40000 ALTER TABLE `loan_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `loan_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `member_id` varchar(20) NOT NULL,
  `member_name` varchar(100) NOT NULL,
  `gender` int(11) NOT NULL,
  `birth_date` date DEFAULT NULL,
  `member_type_id` int(11) DEFAULT NULL,
  `member_address` varchar(255) DEFAULT NULL,
  `member_mail_address` varchar(255) DEFAULT NULL,
  `member_email` varchar(100) DEFAULT NULL,
  `postal_code` varchar(20) DEFAULT NULL,
  `inst_name` varchar(100) DEFAULT NULL,
  `is_new` int(11) DEFAULT NULL,
  `member_image` varchar(200) DEFAULT NULL,
  `pin` varchar(50) DEFAULT NULL,
  `member_phone` varchar(50) DEFAULT NULL,
  `member_fax` varchar(50) DEFAULT NULL,
  `member_since_date` date DEFAULT NULL,
  `register_date` date DEFAULT NULL,
  `expire_date` date NOT NULL,
  `member_notes` longtext DEFAULT NULL,
  `is_pending` smallint(6) NOT NULL,
  `mpasswd` varchar(255) DEFAULT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `last_login_ip` varchar(20) DEFAULT NULL,
  `input_date` date DEFAULT NULL,
  `last_update` date DEFAULT NULL,
  `birth_place` varchar(100) DEFAULT NULL,
  `ktp_image` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`member_id`),
  KEY `member_member__d7211b_idx` (`member_name`),
  KEY `member_member__acfc92_idx` (`member_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES
('12121212212121212','dimas',1,'2004-12-12',1,'pamekasan',NULL,'danibaret014@gmail.com',NULL,'uim',NULL,'',NULL,'0898774848393',NULL,NULL,'2025-09-18','2026-09-18',NULL,1,'pbkdf2_sha256$1000000$V7hWZrdJlye8IlzGMTdj9Y$sr2+uJQaifoO1BS3WBf4YX0biyu/EaM8mPR5THuy+Sk=',NULL,NULL,NULL,NULL,'pamekasan',''),
('1234567890123456','John Doe',1,'1990-01-15',1,'Jl. Sudirman No. 123, Jakarta',NULL,'john.doe@example.com',NULL,'Universitas Indonesia',NULL,'',NULL,'081234567890',NULL,NULL,'2025-09-17','2026-09-17',NULL,1,'pbkdf2_sha256$260000$t4gQvlCdpjmmR1UjlPNtAJ$WZWc/XRoE58NXLUeeyZe0tDDHviUxBRzEglCHof9z2k=',NULL,NULL,NULL,NULL,'Jakarta',''),
('3528012345678910','yahya',1,'1990-05-15',1,'Jl. Sudirman No. 123, pamekasan',NULL,'sajakcodingan@example.com',NULL,'Universitas Indonesia',NULL,'',NULL,'081234567890',NULL,NULL,'2025-09-18','2026-09-18',NULL,0,'pbkdf2_sha256$1000000$I7n5BwB6SnTrO3WsQeiCuP$Y6uRt4cHCh2Zuj/o0AEzV6iqPkiVpVLpnhXxRObxqBY=',NULL,NULL,NULL,NULL,'pamekasan',''),
('string','string',1,'2025-09-22',1,'string',NULL,'user@example.com',NULL,'string',NULL,'string',NULL,'string',NULL,NULL,'2025-09-22','2026-09-22',NULL,1,'pbkdf2_sha256$1000000$OyqOLxrpiUesWa4vf58McO$981tsKx99vb/QGz5oTQSr0EA/F8rXpRFgqmfNFQQMGc=',NULL,NULL,NULL,NULL,'string','string');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member_custom`
--

DROP TABLE IF EXISTS `member_custom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `member_custom` (
  `member_id` varchar(20) NOT NULL,
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member_custom`
--

LOCK TABLES `member_custom` WRITE;
/*!40000 ALTER TABLE `member_custom` DISABLE KEYS */;
/*!40000 ALTER TABLE `member_custom` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mst_author`
--

DROP TABLE IF EXISTS `mst_author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `mst_author` (
  `author_id` int(11) NOT NULL AUTO_INCREMENT,
  `author_name` varchar(100) NOT NULL,
  `author_year` varchar(20) DEFAULT NULL,
  `authority_type` varchar(1) NOT NULL,
  `auth_list` varchar(20) DEFAULT NULL,
  `input_date` date NOT NULL,
  `last_update` date DEFAULT NULL,
  PRIMARY KEY (`author_id`),
  UNIQUE KEY `author_name` (`author_name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mst_author`
--

LOCK TABLES `mst_author` WRITE;
/*!40000 ALTER TABLE `mst_author` DISABLE KEYS */;
INSERT INTO `mst_author` VALUES
(1,'John Doe',NULL,'p',NULL,'2025-12-13',NULL);
/*!40000 ALTER TABLE `mst_author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mst_carrier_type`
--

DROP TABLE IF EXISTS `mst_carrier_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `mst_carrier_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `carrier_type` varchar(100) NOT NULL,
  `code` varchar(5) NOT NULL,
  `code2` varchar(1) NOT NULL,
  `input_date` datetime(6) NOT NULL,
  `last_update` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `carrier_type` (`carrier_type`),
  KEY `mst_carrier_code_0467da_idx` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mst_carrier_type`
--

LOCK TABLES `mst_carrier_type` WRITE;
/*!40000 ALTER TABLE `mst_carrier_type` DISABLE KEYS */;
/*!40000 ALTER TABLE `mst_carrier_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mst_coll_type`
--

DROP TABLE IF EXISTS `mst_coll_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `mst_coll_type` (
  `coll_type_id` int(11) NOT NULL AUTO_INCREMENT,
  `coll_type_name` varchar(30) NOT NULL,
  `input_date` date DEFAULT NULL,
  `last_update` date DEFAULT NULL,
  PRIMARY KEY (`coll_type_id`),
  UNIQUE KEY `coll_type_name` (`coll_type_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mst_coll_type`
--

LOCK TABLES `mst_coll_type` WRITE;
/*!40000 ALTER TABLE `mst_coll_type` DISABLE KEYS */;
/*!40000 ALTER TABLE `mst_coll_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mst_content_type`
--

DROP TABLE IF EXISTS `mst_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `mst_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content_type` varchar(100) NOT NULL,
  `code` varchar(5) NOT NULL,
  `code2` varchar(1) NOT NULL,
  `input_date` datetime(6) NOT NULL,
  `last_update` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type` (`content_type`),
  KEY `mst_content_code_e321db_idx` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mst_content_type`
--

LOCK TABLES `mst_content_type` WRITE;
/*!40000 ALTER TABLE `mst_content_type` DISABLE KEYS */;
/*!40000 ALTER TABLE `mst_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mst_custom_field`
--

DROP TABLE IF EXISTS `mst_custom_field`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `mst_custom_field` (
  `field_id` int(11) NOT NULL AUTO_INCREMENT,
  `primary_table` varchar(100) DEFAULT NULL,
  `dbfield` varchar(50) NOT NULL,
  `label` varchar(80) NOT NULL,
  `type` varchar(20) NOT NULL,
  `default` varchar(80) DEFAULT NULL,
  `max` int(11) DEFAULT NULL,
  `data` longtext DEFAULT NULL,
  `indexed` smallint(6) DEFAULT NULL,
  `class_field` varchar(100) DEFAULT NULL,
  `is_public` smallint(6) DEFAULT NULL,
  `width` int(11) NOT NULL,
  `note` longtext DEFAULT NULL,
  PRIMARY KEY (`field_id`),
  UNIQUE KEY `dbfield` (`dbfield`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mst_custom_field`
--

LOCK TABLES `mst_custom_field` WRITE;
/*!40000 ALTER TABLE `mst_custom_field` DISABLE KEYS */;
/*!40000 ALTER TABLE `mst_custom_field` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mst_frequency`
--

DROP TABLE IF EXISTS `mst_frequency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `mst_frequency` (
  `frequency_id` int(11) NOT NULL AUTO_INCREMENT,
  `frequency` varchar(25) NOT NULL,
  `language_prefix` varchar(5) DEFAULT NULL,
  `time_increment` smallint(6) DEFAULT NULL,
  `time_unit` varchar(10) NOT NULL,
  `input_date` date NOT NULL,
  `last_update` date NOT NULL,
  PRIMARY KEY (`frequency_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mst_frequency`
--

LOCK TABLES `mst_frequency` WRITE;
/*!40000 ALTER TABLE `mst_frequency` DISABLE KEYS */;
/*!40000 ALTER TABLE `mst_frequency` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mst_gmd`
--

DROP TABLE IF EXISTS `mst_gmd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `mst_gmd` (
  `gmd_id` int(11) NOT NULL AUTO_INCREMENT,
  `gmd_code` varchar(3) DEFAULT NULL,
  `gmd_name` varchar(30) NOT NULL,
  `icon_image` varchar(100) DEFAULT NULL,
  `input_date` date NOT NULL,
  `last_update` date DEFAULT NULL,
  PRIMARY KEY (`gmd_id`),
  UNIQUE KEY `gmd_name` (`gmd_name`),
  UNIQUE KEY `gmd_code` (`gmd_code`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mst_gmd`
--

LOCK TABLES `mst_gmd` WRITE;
/*!40000 ALTER TABLE `mst_gmd` DISABLE KEYS */;
INSERT INTO `mst_gmd` VALUES
(1,'BK','Book',NULL,'2025-12-13',NULL);
/*!40000 ALTER TABLE `mst_gmd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mst_item_status`
--

DROP TABLE IF EXISTS `mst_item_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `mst_item_status` (
  `item_status_id` varchar(3) NOT NULL,
  `item_status_name` varchar(30) NOT NULL,
  `rules` varchar(255) DEFAULT NULL,
  `no_loan` smallint(6) NOT NULL,
  `skip_stock_take` smallint(6) NOT NULL,
  `input_date` date DEFAULT NULL,
  `last_update` date DEFAULT NULL,
  PRIMARY KEY (`item_status_id`),
  UNIQUE KEY `item_status_name` (`item_status_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mst_item_status`
--

LOCK TABLES `mst_item_status` WRITE;
/*!40000 ALTER TABLE `mst_item_status` DISABLE KEYS */;
/*!40000 ALTER TABLE `mst_item_status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mst_label`
--

DROP TABLE IF EXISTS `mst_label`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `mst_label` (
  `label_id` int(11) NOT NULL AUTO_INCREMENT,
  `label_name` varchar(20) NOT NULL,
  `label_desc` varchar(50) DEFAULT NULL,
  `label_image` varchar(200) NOT NULL,
  `input_date` date NOT NULL,
  `last_update` date NOT NULL,
  PRIMARY KEY (`label_id`),
  UNIQUE KEY `label_name` (`label_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mst_label`
--

LOCK TABLES `mst_label` WRITE;
/*!40000 ALTER TABLE `mst_label` DISABLE KEYS */;
/*!40000 ALTER TABLE `mst_label` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mst_language`
--

DROP TABLE IF EXISTS `mst_language`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `mst_language` (
  `language_id` varchar(5) NOT NULL,
  `language_name` varchar(20) NOT NULL,
  `input_date` date DEFAULT NULL,
  `last_update` date DEFAULT NULL,
  PRIMARY KEY (`language_id`),
  UNIQUE KEY `language_name` (`language_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mst_language`
--

LOCK TABLES `mst_language` WRITE;
/*!40000 ALTER TABLE `mst_language` DISABLE KEYS */;
/*!40000 ALTER TABLE `mst_language` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mst_loan_rules`
--

DROP TABLE IF EXISTS `mst_loan_rules`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `mst_loan_rules` (
  `loan_rules_id` int(11) NOT NULL AUTO_INCREMENT,
  `member_type_id` int(11) NOT NULL,
  `coll_type_id` int(11) NOT NULL,
  `gmd_id` int(11) NOT NULL,
  `loan_limit` int(11) NOT NULL,
  `loan_periode` int(11) NOT NULL,
  `reborrow_limit` int(11) NOT NULL,
  `fine_each_day` int(11) NOT NULL,
  `grace_periode` smallint(6) NOT NULL,
  `input_date` date DEFAULT NULL,
  `last_update` date DEFAULT NULL,
  PRIMARY KEY (`loan_rules_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mst_loan_rules`
--

LOCK TABLES `mst_loan_rules` WRITE;
/*!40000 ALTER TABLE `mst_loan_rules` DISABLE KEYS */;
/*!40000 ALTER TABLE `mst_loan_rules` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mst_location`
--

DROP TABLE IF EXISTS `mst_location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `mst_location` (
  `location_id` varchar(3) NOT NULL,
  `location_name` varchar(100) DEFAULT NULL,
  `input_date` date NOT NULL,
  `last_update` date NOT NULL,
  PRIMARY KEY (`location_id`),
  UNIQUE KEY `location_name` (`location_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mst_location`
--

LOCK TABLES `mst_location` WRITE;
/*!40000 ALTER TABLE `mst_location` DISABLE KEYS */;
/*!40000 ALTER TABLE `mst_location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mst_media_type`
--

DROP TABLE IF EXISTS `mst_media_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `mst_media_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `media_type` varchar(100) NOT NULL,
  `code` varchar(5) NOT NULL,
  `code2` varchar(1) NOT NULL,
  `input_date` datetime(6) NOT NULL,
  `last_update` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `media_type` (`media_type`),
  KEY `mst_media_t_code_83afca_idx` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mst_media_type`
--

LOCK TABLES `mst_media_type` WRITE;
/*!40000 ALTER TABLE `mst_media_type` DISABLE KEYS */;
/*!40000 ALTER TABLE `mst_media_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mst_member_type`
--

DROP TABLE IF EXISTS `mst_member_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `mst_member_type` (
  `member_type_id` int(11) NOT NULL AUTO_INCREMENT,
  `member_type_name` varchar(50) NOT NULL,
  `loan_limit` int(11) NOT NULL,
  `loan_periode` int(11) NOT NULL,
  `enable_reserve` int(11) NOT NULL,
  `reserve_limit` int(11) NOT NULL,
  `member_periode` int(11) NOT NULL,
  `reborrow_limit` int(11) NOT NULL,
  `fine_each_day` int(11) NOT NULL,
  `grace_periode` smallint(6) NOT NULL,
  `input_date` date NOT NULL,
  `last_update` date DEFAULT NULL,
  PRIMARY KEY (`member_type_id`),
  UNIQUE KEY `member_type_name` (`member_type_name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mst_member_type`
--

LOCK TABLES `mst_member_type` WRITE;
/*!40000 ALTER TABLE `mst_member_type` DISABLE KEYS */;
INSERT INTO `mst_member_type` VALUES
(1,'Mahasiswa',3,7,1,2,365,2,500,3,'2025-09-17','2025-09-17'),
(2,'Dosen',5,14,1,5,365,3,1000,7,'2025-09-17','2025-09-17'),
(3,'Staff',4,10,1,3,365,2,750,5,'2025-09-17','2025-09-17'),
(4,'Umum',2,7,0,1,180,1,1000,3,'2025-09-17','2025-09-17');
/*!40000 ALTER TABLE `mst_member_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mst_module`
--

DROP TABLE IF EXISTS `mst_module`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `mst_module` (
  `module_id` int(11) NOT NULL AUTO_INCREMENT,
  `module_name` varchar(50) NOT NULL,
  `module_path` varchar(200) DEFAULT NULL,
  `module_desc` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`module_id`),
  UNIQUE KEY `module_name` (`module_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mst_module`
--

LOCK TABLES `mst_module` WRITE;
/*!40000 ALTER TABLE `mst_module` DISABLE KEYS */;
/*!40000 ALTER TABLE `mst_module` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mst_place`
--

DROP TABLE IF EXISTS `mst_place`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `mst_place` (
  `place_id` int(11) NOT NULL AUTO_INCREMENT,
  `place_name` varchar(30) NOT NULL,
  `input_date` date DEFAULT NULL,
  `last_update` date DEFAULT NULL,
  PRIMARY KEY (`place_id`),
  UNIQUE KEY `place_name` (`place_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mst_place`
--

LOCK TABLES `mst_place` WRITE;
/*!40000 ALTER TABLE `mst_place` DISABLE KEYS */;
/*!40000 ALTER TABLE `mst_place` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mst_publisher`
--

DROP TABLE IF EXISTS `mst_publisher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `mst_publisher` (
  `publisher_id` int(11) NOT NULL AUTO_INCREMENT,
  `publisher_name` varchar(100) NOT NULL,
  `input_date` date DEFAULT NULL,
  `last_update` date DEFAULT NULL,
  PRIMARY KEY (`publisher_id`),
  UNIQUE KEY `publisher_name` (`publisher_name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mst_publisher`
--

LOCK TABLES `mst_publisher` WRITE;
/*!40000 ALTER TABLE `mst_publisher` DISABLE KEYS */;
INSERT INTO `mst_publisher` VALUES
(1,'Sample Publisher','2025-12-13',NULL);
/*!40000 ALTER TABLE `mst_publisher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mst_relation_term`
--

DROP TABLE IF EXISTS `mst_relation_term`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `mst_relation_term` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rt_id` varchar(11) NOT NULL,
  `rt_desc` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mst_relation_term`
--

LOCK TABLES `mst_relation_term` WRITE;
/*!40000 ALTER TABLE `mst_relation_term` DISABLE KEYS */;
/*!40000 ALTER TABLE `mst_relation_term` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mst_servers`
--

DROP TABLE IF EXISTS `mst_servers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `mst_servers` (
  `server_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `uri` longtext NOT NULL,
  `server_type` smallint(6) NOT NULL,
  `input_date` datetime(6) NOT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`server_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mst_servers`
--

LOCK TABLES `mst_servers` WRITE;
/*!40000 ALTER TABLE `mst_servers` DISABLE KEYS */;
/*!40000 ALTER TABLE `mst_servers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mst_supplier`
--

DROP TABLE IF EXISTS `mst_supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `mst_supplier` (
  `supplier_id` int(11) NOT NULL AUTO_INCREMENT,
  `supplier_name` varchar(100) NOT NULL,
  `address` varchar(100) DEFAULT NULL,
  `postal_code` varchar(10) DEFAULT NULL,
  `phone` varchar(14) DEFAULT NULL,
  `contact` varchar(30) DEFAULT NULL,
  `fax` varchar(14) DEFAULT NULL,
  `account` varchar(12) DEFAULT NULL,
  `e_mail` varchar(80) DEFAULT NULL,
  `input_date` date DEFAULT NULL,
  `last_update` date DEFAULT NULL,
  PRIMARY KEY (`supplier_id`),
  UNIQUE KEY `supplier_name` (`supplier_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mst_supplier`
--

LOCK TABLES `mst_supplier` WRITE;
/*!40000 ALTER TABLE `mst_supplier` DISABLE KEYS */;
/*!40000 ALTER TABLE `mst_supplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mst_topic`
--

DROP TABLE IF EXISTS `mst_topic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `mst_topic` (
  `topic_id` int(11) NOT NULL AUTO_INCREMENT,
  `topic` varchar(50) NOT NULL,
  `topic_type` varchar(2) NOT NULL,
  `auth_list` varchar(20) DEFAULT NULL,
  `classification` varchar(50) NOT NULL,
  `input_date` date DEFAULT NULL,
  `last_update` date DEFAULT NULL,
  PRIMARY KEY (`topic_id`),
  UNIQUE KEY `topic` (`topic`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mst_topic`
--

LOCK TABLES `mst_topic` WRITE;
/*!40000 ALTER TABLE `mst_topic` DISABLE KEYS */;
/*!40000 ALTER TABLE `mst_topic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mst_voc_ctrl`
--

DROP TABLE IF EXISTS `mst_voc_ctrl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `mst_voc_ctrl` (
  `vocabolary_id` int(11) NOT NULL AUTO_INCREMENT,
  `topic_id` int(11) NOT NULL,
  `rt_id` varchar(11) NOT NULL,
  `related_topic_id` varchar(250) NOT NULL,
  `scope` longtext DEFAULT NULL,
  PRIMARY KEY (`vocabolary_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mst_voc_ctrl`
--

LOCK TABLES `mst_voc_ctrl` WRITE;
/*!40000 ALTER TABLE `mst_voc_ctrl` DISABLE KEYS */;
/*!40000 ALTER TABLE `mst_voc_ctrl` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plugins`
--

DROP TABLE IF EXISTS `plugins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `plugins` (
  `id` varchar(32) NOT NULL,
  `path` longtext NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `uid` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plugins`
--

LOCK TABLES `plugins` WRITE;
/*!40000 ALTER TABLE `plugins` DISABLE KEYS */;
/*!40000 ALTER TABLE `plugins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reserve`
--

DROP TABLE IF EXISTS `reserve`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `reserve` (
  `reserve_id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` varchar(20) NOT NULL,
  `biblio_id` int(11) NOT NULL,
  `item_code` varchar(20) NOT NULL,
  `reserve_date` datetime(6) NOT NULL,
  PRIMARY KEY (`reserve_id`),
  KEY `reserve_member__aad5e2_idx` (`member_id`,`biblio_id`),
  KEY `reserve_item_co_2e491e_idx` (`item_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reserve`
--

LOCK TABLES `reserve` WRITE;
/*!40000 ALTER TABLE `reserve` DISABLE KEYS */;
/*!40000 ALTER TABLE `reserve` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `search_biblio`
--

DROP TABLE IF EXISTS `search_biblio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `search_biblio` (
  `biblio_id` int(11) NOT NULL,
  `title` longtext DEFAULT NULL,
  `edition` varchar(50) DEFAULT NULL,
  `isbn_issn` varchar(20) DEFAULT NULL,
  `author` longtext DEFAULT NULL,
  `topic` longtext DEFAULT NULL,
  `gmd` varchar(30) DEFAULT NULL,
  `publisher` varchar(100) DEFAULT NULL,
  `publish_place` varchar(30) DEFAULT NULL,
  `language` varchar(20) DEFAULT NULL,
  `classification` varchar(40) DEFAULT NULL,
  `spec_detail_info` longtext DEFAULT NULL,
  `carrier_type` varchar(100) NOT NULL,
  `content_type` varchar(100) NOT NULL,
  `media_type` varchar(100) NOT NULL,
  `location` longtext DEFAULT NULL,
  `publish_year` varchar(20) DEFAULT NULL,
  `notes` longtext DEFAULT NULL,
  `series_title` longtext DEFAULT NULL,
  `items` longtext DEFAULT NULL,
  `collection_types` longtext DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `opac_hide` smallint(6) NOT NULL,
  `promoted` smallint(6) NOT NULL,
  `labels` longtext DEFAULT NULL,
  `collation` varchar(100) DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL,
  `input_date` datetime(6) DEFAULT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`biblio_id`),
  KEY `search_bibl_gmd_d04b9c_idx` (`gmd`,`publisher`,`publish_place`,`language`,`classification`,`publish_year`,`call_number`),
  KEY `search_bibl_opac_hi_bd1518_idx` (`opac_hide`,`promoted`),
  KEY `search_bibl_carrier_3eb08d_idx` (`carrier_type`,`media_type`,`content_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `search_biblio`
--

LOCK TABLES `search_biblio` WRITE;
/*!40000 ALTER TABLE `search_biblio` DISABLE KEYS */;
/*!40000 ALTER TABLE `search_biblio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `serial`
--

DROP TABLE IF EXISTS `serial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `serial` (
  `serial_id` int(11) NOT NULL AUTO_INCREMENT,
  `date_start` date NOT NULL,
  `date_end` date DEFAULT NULL,
  `period` varchar(100) DEFAULT NULL,
  `notes` longtext DEFAULT NULL,
  `biblio_id` int(11) DEFAULT NULL,
  `gmd_id` int(11) DEFAULT NULL,
  `input_date` date NOT NULL,
  `last_update` date NOT NULL,
  PRIMARY KEY (`serial_id`),
  KEY `serial_biblio__b519df_idx` (`biblio_id`),
  KEY `serial_gmd_id_528908_idx` (`gmd_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `serial`
--

LOCK TABLES `serial` WRITE;
/*!40000 ALTER TABLE `serial` DISABLE KEYS */;
/*!40000 ALTER TABLE `serial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `setting`
--

DROP TABLE IF EXISTS `setting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `setting` (
  `setting_id` int(11) NOT NULL AUTO_INCREMENT,
  `setting_name` varchar(30) NOT NULL,
  `setting_value` longtext DEFAULT NULL,
  PRIMARY KEY (`setting_id`),
  UNIQUE KEY `setting_name` (`setting_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `setting`
--

LOCK TABLES `setting` WRITE;
/*!40000 ALTER TABLE `setting` DISABLE KEYS */;
/*!40000 ALTER TABLE `setting` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stock_take`
--

DROP TABLE IF EXISTS `stock_take`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `stock_take` (
  `stock_take_id` int(11) NOT NULL AUTO_INCREMENT,
  `stock_take_name` varchar(200) NOT NULL,
  `start_date` datetime(6) NOT NULL,
  `end_date` datetime(6) DEFAULT NULL,
  `init_user` varchar(50) NOT NULL,
  `total_item_stock_taked` int(11) DEFAULT NULL,
  `total_item_lost` int(11) DEFAULT NULL,
  `total_item_exists` int(11) NOT NULL,
  `total_item_loan` int(11) DEFAULT NULL,
  `stock_take_users` longtext DEFAULT NULL,
  `is_active` int(11) NOT NULL,
  `report_file` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`stock_take_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stock_take`
--

LOCK TABLES `stock_take` WRITE;
/*!40000 ALTER TABLE `stock_take` DISABLE KEYS */;
/*!40000 ALTER TABLE `stock_take` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stock_take_item`
--

DROP TABLE IF EXISTS `stock_take_item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `stock_take_item` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `stock_take_id` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  `item_code` varchar(20) NOT NULL,
  `title` varchar(255) NOT NULL,
  `gmd_name` varchar(30) DEFAULT NULL,
  `classification` varchar(30) DEFAULT NULL,
  `coll_type_name` varchar(30) DEFAULT NULL,
  `call_number` varchar(50) DEFAULT NULL,
  `location` varchar(100) DEFAULT NULL,
  `status` varchar(10) NOT NULL,
  `checked_by` varchar(50) NOT NULL,
  `last_update` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `stock_take_item_stock_take_id_item_id_ce5b9395_uniq` (`stock_take_id`,`item_id`),
  KEY `stock_take__item_co_0c2279_idx` (`item_code`),
  KEY `stock_take__status_a16195_idx` (`status`),
  KEY `stock_take__gmd_nam_273ab0_idx` (`gmd_name`,`classification`,`coll_type_name`,`location`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stock_take_item`
--

LOCK TABLES `stock_take_item` WRITE;
/*!40000 ALTER TABLE `stock_take_item` DISABLE KEYS */;
/*!40000 ALTER TABLE `stock_take_item` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `system_log`
--

DROP TABLE IF EXISTS `system_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `system_log` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT,
  `log_type` varchar(20) NOT NULL,
  `id` varchar(50) DEFAULT NULL,
  `log_location` varchar(50) NOT NULL,
  `sub_module` varchar(50) DEFAULT NULL,
  `action` varchar(50) DEFAULT NULL,
  `log_msg` longtext NOT NULL,
  `log_date` datetime(6) NOT NULL,
  PRIMARY KEY (`log_id`),
  KEY `system_log_log_typ_822019_idx` (`log_type`),
  KEY `system_log_id_306723_idx` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `system_log`
--

LOCK TABLES `system_log` WRITE;
/*!40000 ALTER TABLE `system_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `system_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `realname` varchar(100) NOT NULL,
  `passwd` varchar(255) NOT NULL,
  `fa` longtext DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `user_type` smallint(6) DEFAULT NULL,
  `user_image` varchar(250) DEFAULT NULL,
  `social_media` longtext DEFAULT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `last_login_ip` varchar(15) DEFAULT NULL,
  `groups` varchar(200) DEFAULT NULL,
  `forgot` varchar(80) DEFAULT NULL,
  `admin_template` longtext DEFAULT NULL,
  `input_date` date DEFAULT NULL,
  `last_update` date DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES
(1,'1234567890123456','John Doe','pbkdf2_sha256$260000$t4gQvlCdpjmmR1UjlPNtAJ$WZWc/XRoE58NXLUeeyZe0tDDHviUxBRzEglCHof9z2k=',NULL,'john.doe@example.com',2,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
(2,'admin123','Administrator','adminpassword123',NULL,'admin@library.com',1,'','',NULL,NULL,'1',NULL,NULL,NULL,NULL),
(3,'12121212212121212','dimas','pbkdf2_sha256$1000000$V7hWZrdJlye8IlzGMTdj9Y$sr2+uJQaifoO1BS3WBf4YX0biyu/EaM8mPR5THuy+Sk=',NULL,'danibaret014@gmail.com',2,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
(4,'3528012345678910','yahya','pbkdf2_sha256$1000000$I7n5BwB6SnTrO3WsQeiCuP$Y6uRt4cHCh2Zuj/o0AEzV6iqPkiVpVLpnhXxRObxqBY=',NULL,'sajakcodingan@example.com',2,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
(5,'string','string','pbkdf2_sha256$1000000$OyqOLxrpiUesWa4vf58McO$981tsKx99vb/QGz5oTQSr0EA/F8rXpRFgqmfNFQQMGc=',NULL,'user@example.com',2,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_group`
--

DROP TABLE IF EXISTS `user_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_group` (
  `group_id` int(11) NOT NULL AUTO_INCREMENT,
  `group_name` varchar(30) NOT NULL,
  `input_date` date DEFAULT NULL,
  `last_update` date DEFAULT NULL,
  PRIMARY KEY (`group_id`),
  UNIQUE KEY `group_name` (`group_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_group`
--

LOCK TABLES `user_group` WRITE;
/*!40000 ALTER TABLE `user_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `visitor_count`
--

DROP TABLE IF EXISTS `visitor_count`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `visitor_count` (
  `visitor_id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` varchar(20) DEFAULT NULL,
  `member_name` varchar(255) NOT NULL,
  `institution` varchar(100) DEFAULT NULL,
  `checkin_date` datetime(6) NOT NULL,
  PRIMARY KEY (`visitor_id`),
  KEY `visitor_cou_member__86f33b_idx` (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visitor_count`
--

LOCK TABLES `visitor_count` WRITE;
/*!40000 ALTER TABLE `visitor_count` DISABLE KEYS */;
/*!40000 ALTER TABLE `visitor_count` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-13 11:51:26
