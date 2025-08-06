/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.33 : Database - gluco_guard
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`gluco_guard` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `gluco_guard`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
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
(25,'Can add dietitian_table',7,'add_dietitian_table'),
(26,'Can change dietitian_table',7,'change_dietitian_table'),
(27,'Can delete dietitian_table',7,'delete_dietitian_table'),
(28,'Can view dietitian_table',7,'view_dietitian_table'),
(29,'Can add login_table',8,'add_login_table'),
(30,'Can change login_table',8,'change_login_table'),
(31,'Can delete login_table',8,'delete_login_table'),
(32,'Can view login_table',8,'view_login_table'),
(33,'Can add dietplan_table',9,'add_dietplan_table'),
(34,'Can change dietplan_table',9,'change_dietplan_table'),
(35,'Can delete dietplan_table',9,'delete_dietplan_table'),
(36,'Can view dietplan_table',9,'view_dietplan_table'),
(37,'Can add doctor_table',10,'add_doctor_table'),
(38,'Can change doctor_table',10,'change_doctor_table'),
(39,'Can delete doctor_table',10,'delete_doctor_table'),
(40,'Can view doctor_table',10,'view_doctor_table'),
(41,'Can add chat_table',11,'add_chat_table'),
(42,'Can change chat_table',11,'change_chat_table'),
(43,'Can delete chat_table',11,'delete_chat_table'),
(44,'Can view chat_table',11,'view_chat_table'),
(45,'Can add schedule_table',12,'add_schedule_table'),
(46,'Can change schedule_table',12,'change_schedule_table'),
(47,'Can delete schedule_table',12,'delete_schedule_table'),
(48,'Can view schedule_table',12,'view_schedule_table'),
(49,'Can add booking_table',13,'add_booking_table'),
(50,'Can change booking_table',13,'change_booking_table'),
(51,'Can delete booking_table',13,'delete_booking_table'),
(52,'Can view booking_table',13,'view_booking_table'),
(53,'Can add tip_table',14,'add_tip_table'),
(54,'Can change tip_table',14,'change_tip_table'),
(55,'Can delete tip_table',14,'delete_tip_table'),
(56,'Can view tip_table',14,'view_tip_table'),
(57,'Can add user_table',15,'add_user_table'),
(58,'Can change user_table',15,'change_user_table'),
(59,'Can delete user_table',15,'delete_user_table'),
(60,'Can view user_table',15,'view_user_table'),
(61,'Can add rating_table',16,'add_rating_table'),
(62,'Can change rating_table',16,'change_rating_table'),
(63,'Can delete rating_table',16,'delete_rating_table'),
(64,'Can view rating_table',16,'view_rating_table'),
(65,'Can add doubt_table',17,'add_doubt_table'),
(66,'Can change doubt_table',17,'change_doubt_table'),
(67,'Can delete doubt_table',17,'delete_doubt_table'),
(68,'Can view doubt_table',17,'view_doubt_table'),
(69,'Can add doctor_rating_table',18,'add_doctor_rating_table'),
(70,'Can change doctor_rating_table',18,'change_doctor_rating_table'),
(71,'Can delete doctor_rating_table',18,'delete_doctor_rating_table'),
(72,'Can view doctor_rating_table',18,'view_doctor_rating_table');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values 
(1,'pbkdf2_sha256$260000$cIAIrUWhXEKDAme8jmFUcJ$v4mxQpq4xc45sulPEIo3v5VXjdLRt0MjGJiFnMnhJxM=','2024-02-14 05:16:17.538919',1,'admin','','','admin@gmail.com',1,1,'2024-02-08 04:26:13.434839'),
(2,'pbkdf2_sha256$260000$D8nwgnz1IHqUELElRI9OqP$4hhqEwvSgBJIfM2zTIl5qz/86VX+/Y3v3t8pHNrXi5k=','2024-02-14 10:24:00.960077',1,'hazna','','','hazna@gmail.com',1,1,'2024-02-14 05:32:01.793733');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(13,'GG_App','booking_table'),
(11,'GG_App','chat_table'),
(7,'GG_App','dietitian_table'),
(9,'GG_App','dietplan_table'),
(18,'GG_App','doctor_rating_table'),
(10,'GG_App','doctor_table'),
(17,'GG_App','doubt_table'),
(8,'GG_App','login_table'),
(16,'GG_App','rating_table'),
(12,'GG_App','schedule_table'),
(14,'GG_App','tip_table'),
(15,'GG_App','user_table'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'GG_App','0001_initial','2024-02-08 04:11:32.819439'),
(2,'GG_App','0002_auto_20240208_0941','2024-02-08 04:11:33.006937'),
(3,'contenttypes','0001_initial','2024-02-08 04:11:33.053800'),
(4,'auth','0001_initial','2024-02-08 04:11:33.491322'),
(5,'admin','0001_initial','2024-02-08 04:11:33.600681'),
(6,'admin','0002_logentry_remove_auto_add','2024-02-08 04:11:33.616346'),
(7,'admin','0003_logentry_add_action_flag_choices','2024-02-08 04:11:33.631985'),
(8,'contenttypes','0002_remove_content_type_name','2024-02-08 04:11:33.710061'),
(9,'auth','0002_alter_permission_name_max_length','2024-02-08 04:11:33.772553'),
(10,'auth','0003_alter_user_email_max_length','2024-02-08 04:11:33.803806'),
(11,'auth','0004_alter_user_username_opts','2024-02-08 04:11:33.819433'),
(12,'auth','0005_alter_user_last_login_null','2024-02-08 04:11:33.866306'),
(13,'auth','0006_require_contenttypes_0002','2024-02-08 04:11:33.866306'),
(14,'auth','0007_alter_validators_add_error_messages','2024-02-08 04:11:33.881937'),
(15,'auth','0008_alter_user_username_max_length','2024-02-08 04:11:33.928803'),
(16,'auth','0009_alter_user_last_name_max_length','2024-02-08 04:11:33.975709'),
(17,'auth','0010_alter_group_name_max_length','2024-02-08 04:11:34.006925'),
(18,'auth','0011_update_proxy_permissions','2024-02-08 04:11:34.022552'),
(19,'auth','0012_alter_user_first_name_max_length','2024-02-08 04:11:34.069426'),
(20,'sessions','0001_initial','2024-02-08 04:11:34.100674'),
(21,'GG_App','0003_auto_20240213_1912','2024-02-13 13:42:37.752906'),
(22,'GG_App','0004_booking_table_user','2024-02-14 05:03:38.012746');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('6gv54j6uw9a7o0tunu11fyh0kcbs6i5m','.eJxVjDsOwjAQBe_iGln-xruU9DmDtV4bHECOFCcV4u4QKQW0b2beS0Ta1hq3XpY4ZXEWWpx-t0T8KG0H-U7tNkue27pMSe6KPGiX45zL83K4fweVev3WDshyQsJh8KCvIRcwnnIIii1pNMGBsgqsYUzGg8OQUGdHBRMDGS_eH8laNyY:1ra7d3:Pz0_-A1CTsFIQTaGn7kLqVSguOmVN7HlHpBY7nle-cY','2024-02-28 05:16:17.538919'),
('x9aj7r4awi3otxh9q16p9sjg3vclgurh','.eJxVjs0OwiAQhN-FsyHALuB69N5nILsFpdq0SX9OxndXkh70Ot_Ml3mpxPtW076WJQ1ZXZRTp99MuH-WqYH84Ok-636etmUQ3Sr6oKvu5lzG69H9E1Re63dtCEQICbwVx87f0BTuPbngDDJkD5CJOTIKUrCAZyyRKRiJYJxt0rH98-8Pf_o45g:1raCQq:OW_MEWTuBbPArZgvHAn0SvA7UT4hTh_VSiIxfmkebMU','2024-02-28 10:24:00.975702');

/*Table structure for table `gg_app_booking_table` */

DROP TABLE IF EXISTS `gg_app_booking_table`;

CREATE TABLE `gg_app_booking_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `time` time(6) NOT NULL,
  `status` varchar(20) NOT NULL,
  `SCHEDULE_id` bigint NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `GG_App_booking_table_SCHEDULE_id_40c83fd9_fk_GG_App_sc` (`SCHEDULE_id`),
  KEY `GG_App_booking_table_USER_id_148fc59b_fk_GG_App_user_table_id` (`USER_id`),
  CONSTRAINT `GG_App_booking_table_SCHEDULE_id_40c83fd9_fk_GG_App_sc` FOREIGN KEY (`SCHEDULE_id`) REFERENCES `gg_app_schedule_table` (`id`),
  CONSTRAINT `GG_App_booking_table_USER_id_148fc59b_fk_GG_App_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `gg_app_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `gg_app_booking_table` */

insert  into `gg_app_booking_table`(`id`,`time`,`status`,`SCHEDULE_id`,`USER_id`) values 
(1,'18:45:57.145420','booked',1,2);

/*Table structure for table `gg_app_chat_table` */

DROP TABLE IF EXISTS `gg_app_chat_table`;

CREATE TABLE `gg_app_chat_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `message` varchar(20) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `FROM_ID_id` bigint NOT NULL,
  `TO_ID_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `GG_App_chat_table_FROM_ID_id_a208da05_fk_GG_App_login_table_id` (`FROM_ID_id`),
  KEY `GG_App_chat_table_TO_ID_id_496bbe7b_fk_GG_App_login_table_id` (`TO_ID_id`),
  CONSTRAINT `GG_App_chat_table_FROM_ID_id_a208da05_fk_GG_App_login_table_id` FOREIGN KEY (`FROM_ID_id`) REFERENCES `gg_app_login_table` (`id`),
  CONSTRAINT `GG_App_chat_table_TO_ID_id_496bbe7b_fk_GG_App_login_table_id` FOREIGN KEY (`TO_ID_id`) REFERENCES `gg_app_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `gg_app_chat_table` */

insert  into `gg_app_chat_table`(`id`,`message`,`date`,`time`,`FROM_ID_id`,`TO_ID_id`) values 
(1,'hiii','2024-02-13','19:33:58.000000',3,5),
(2,'hlo','2024-02-13','19:33:58.000000',5,3),
(3,'ha','2024-02-14','15:54:13.540369',5,3);

/*Table structure for table `gg_app_dietitian_table` */

DROP TABLE IF EXISTS `gg_app_dietitian_table`;

CREATE TABLE `gg_app_dietitian_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `firstname` varchar(20) NOT NULL,
  `qualification` varchar(20) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `dob` varchar(20) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  `lastname` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `GG_App_dietitian_tab_LOGIN_id_ce6e38c0_fk_GG_App_lo` (`LOGIN_id`),
  CONSTRAINT `GG_App_dietitian_tab_LOGIN_id_ce6e38c0_fk_GG_App_lo` FOREIGN KEY (`LOGIN_id`) REFERENCES `gg_app_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `gg_app_dietitian_table` */

insert  into `gg_app_dietitian_table`(`id`,`firstname`,`qualification`,`photo`,`dob`,`gender`,`email`,`LOGIN_id`,`lastname`) values 
(1,'zeba','mbbs','ash_color.jpg','2024-02-23','female','fgngnnge@gmail.com',5,'meharin');

/*Table structure for table `gg_app_dietplan_table` */

DROP TABLE IF EXISTS `gg_app_dietplan_table`;

CREATE TABLE `gg_app_dietplan_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `BMI` double NOT NULL,
  `age` int NOT NULL,
  `gender` varchar(20) NOT NULL,
  `dietplan` varchar(20) NOT NULL,
  `dietition_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `GG_App_dietplan_tabl_dietition_id_e445a932_fk_GG_App_di` (`dietition_id`),
  CONSTRAINT `GG_App_dietplan_tabl_dietition_id_e445a932_fk_GG_App_di` FOREIGN KEY (`dietition_id`) REFERENCES `gg_app_dietitian_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `gg_app_dietplan_table` */

insert  into `gg_app_dietplan_table`(`id`,`BMI`,`age`,`gender`,`dietplan`,`dietition_id`) values 
(1,30,12,'male','dknbcb',1);

/*Table structure for table `gg_app_doctor_rating_table` */

DROP TABLE IF EXISTS `gg_app_doctor_rating_table`;

CREATE TABLE `gg_app_doctor_rating_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rating` double NOT NULL,
  `date` date NOT NULL,
  `review` varchar(20) NOT NULL,
  `DOCTOR_id` bigint NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `GG_App_doctor_rating_DOCTOR_id_e14175f4_fk_GG_App_do` (`DOCTOR_id`),
  KEY `GG_App_doctor_rating_USER_id_62df2086_fk_GG_App_us` (`USER_id`),
  CONSTRAINT `GG_App_doctor_rating_DOCTOR_id_e14175f4_fk_GG_App_do` FOREIGN KEY (`DOCTOR_id`) REFERENCES `gg_app_doctor_table` (`id`),
  CONSTRAINT `GG_App_doctor_rating_USER_id_62df2086_fk_GG_App_us` FOREIGN KEY (`USER_id`) REFERENCES `gg_app_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `gg_app_doctor_rating_table` */

insert  into `gg_app_doctor_rating_table`(`id`,`rating`,`date`,`review`,`DOCTOR_id`,`USER_id`) values 
(1,4.5,'2024-02-13','hhhfsgh',1,1);

/*Table structure for table `gg_app_doctor_table` */

DROP TABLE IF EXISTS `gg_app_doctor_table`;

CREATE TABLE `gg_app_doctor_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `firstname` varchar(20) NOT NULL,
  `qualification` varchar(20) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `dob` varchar(20) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  `lastname` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `GG_App_doctor_table_LOGIN_id_076e033f_fk_GG_App_login_table_id` (`LOGIN_id`),
  CONSTRAINT `GG_App_doctor_table_LOGIN_id_076e033f_fk_GG_App_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `gg_app_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `gg_app_doctor_table` */

insert  into `gg_app_doctor_table`(`id`,`firstname`,`qualification`,`photo`,`dob`,`gender`,`email`,`LOGIN_id`,`lastname`) values 
(1,'leela','mbbs','frf','12-02-24','female','hhgug@gmail.com',2,'kumari'),
(2,'subhramani','mbbs','allowvisitor.png','2024-02-13','Male','hgfh@gmail.com',6,'kpp');

/*Table structure for table `gg_app_doubt_table` */

DROP TABLE IF EXISTS `gg_app_doubt_table`;

CREATE TABLE `gg_app_doubt_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `doubt` varchar(20) NOT NULL,
  `reply` varchar(20) NOT NULL,
  `date` date NOT NULL,
  `DOC_ID_id` bigint NOT NULL,
  `UID_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `GG_App_doubt_table_DOC_ID_id_2f9ed3f9_fk_GG_App_doctor_table_id` (`DOC_ID_id`),
  KEY `GG_App_doubt_table_UID_id_aa49d2e9_fk_GG_App_user_table_id` (`UID_id`),
  CONSTRAINT `GG_App_doubt_table_DOC_ID_id_2f9ed3f9_fk_GG_App_doctor_table_id` FOREIGN KEY (`DOC_ID_id`) REFERENCES `gg_app_doctor_table` (`id`),
  CONSTRAINT `GG_App_doubt_table_UID_id_aa49d2e9_fk_GG_App_user_table_id` FOREIGN KEY (`UID_id`) REFERENCES `gg_app_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `gg_app_doubt_table` */

insert  into `gg_app_doubt_table`(`id`,`doubt`,`reply`,`date`,`DOC_ID_id`,`UID_id`) values 
(1,'hhh','pending','2024-02-13',1,1);

/*Table structure for table `gg_app_login_table` */

DROP TABLE IF EXISTS `gg_app_login_table`;

CREATE TABLE `gg_app_login_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `type` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `gg_app_login_table` */

insert  into `gg_app_login_table`(`id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'bbbb','12345678','doctor'),
(3,'aaa','aaa','user'),
(4,'aaa','12345678','user'),
(5,'diet','diet','dietitian'),
(6,'sub','sub','doctor');

/*Table structure for table `gg_app_rating_table` */

DROP TABLE IF EXISTS `gg_app_rating_table`;

CREATE TABLE `gg_app_rating_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `rating` double NOT NULL,
  `date` date NOT NULL,
  `review` varchar(20) NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `GG_App_rating_table_USER_id_c93794f8_fk_GG_App_user_table_id` (`USER_id`),
  CONSTRAINT `GG_App_rating_table_USER_id_c93794f8_fk_GG_App_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `gg_app_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `gg_app_rating_table` */

insert  into `gg_app_rating_table`(`id`,`rating`,`date`,`review`,`USER_id`) values 
(1,3,'2024-02-13','good',1);

/*Table structure for table `gg_app_schedule_table` */

DROP TABLE IF EXISTS `gg_app_schedule_table`;

CREATE TABLE `gg_app_schedule_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `from_time` time(6) NOT NULL,
  `to_time` time(6) NOT NULL,
  `DOC_ID_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `GG_App_schedule_tabl_DOC_ID_id_543edada_fk_GG_App_do` (`DOC_ID_id`),
  CONSTRAINT `GG_App_schedule_tabl_DOC_ID_id_543edada_fk_GG_App_do` FOREIGN KEY (`DOC_ID_id`) REFERENCES `gg_app_doctor_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `gg_app_schedule_table` */

insert  into `gg_app_schedule_table`(`id`,`date`,`from_time`,`to_time`,`DOC_ID_id`) values 
(1,'2024-02-13','00:00:09.000000','00:00:01.000000',1);

/*Table structure for table `gg_app_tip_table` */

DROP TABLE IF EXISTS `gg_app_tip_table`;

CREATE TABLE `gg_app_tip_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `tips` varchar(20) NOT NULL,
  `date` date NOT NULL,
  `time` time(6) NOT NULL,
  `DIETITION_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `GG_App_tip_table_DIETITION_id_1ef250c2_fk_GG_App_di` (`DIETITION_id`),
  CONSTRAINT `GG_App_tip_table_DIETITION_id_1ef250c2_fk_GG_App_di` FOREIGN KEY (`DIETITION_id`) REFERENCES `gg_app_dietitian_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `gg_app_tip_table` */

insert  into `gg_app_tip_table`(`id`,`tips`,`date`,`time`,`DIETITION_id`) values 
(1,'dfhjrgfu','2024-02-13','00:00:02.000000',1);

/*Table structure for table `gg_app_user_table` */

DROP TABLE IF EXISTS `gg_app_user_table`;

CREATE TABLE `gg_app_user_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `age` int NOT NULL,
  `gender` varchar(20) NOT NULL,
  `photo` varchar(100) NOT NULL,
  `address` varchar(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `weight` double NOT NULL,
  `height` double NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `GG_App_user_table_LOGIN_id_3ded382e_fk_GG_App_login_table_id` (`LOGIN_id`),
  CONSTRAINT `GG_App_user_table_LOGIN_id_3ded382e_fk_GG_App_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `gg_app_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `gg_app_user_table` */

insert  into `gg_app_user_table`(`id`,`first_name`,`last_name`,`age`,`gender`,`photo`,`address`,`email`,`weight`,`height`,`LOGIN_id`) values 
(1,'cvc','dyys',23,'FEMALE','IMG-20240207-WA0002.jpg','bdbhs','dndneh@gmail.com',50,154,3),
(2,'cvc','dyys',23,'FEMALE','IMG-20240207-WA0002_ykZTQYM.jpg','bdbhs','dndneh@gmail.com',50,154,4);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
