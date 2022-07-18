-- MariaDB dump 10.19  Distrib 10.5.12-MariaDB, for Linux (x86_64)
--
-- Host: mysql.hostinger.ro    Database: u574849695_23
-- ------------------------------------------------------
-- Server version	10.5.12-MariaDB-cll-lve

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
-- Table structure for table `deliveries_log`
--

DROP TABLE IF EXISTS `deliveries_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deliveries_log` (
  `shipment_id` int(11) NOT NULL AUTO_INCREMENT,
  `expected_delivery_date` date DEFAULT NULL,
  `actual_delivery_date` date DEFAULT NULL,
  `supplier_id` int(11) NOT NULL,
  PRIMARY KEY (`shipment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deliveries_log`
--

LOCK TABLES `deliveries_log` WRITE;
/*!40000 ALTER TABLE `deliveries_log` DISABLE KEYS */;
INSERT INTO `deliveries_log` VALUES (1,'1970-01-01','1970-01-01',1),(2,'1970-01-01','1970-01-01',2),(3,'1970-01-01','1970-01-01',3),(4,'1970-01-01','1970-01-01',1),(5,'1970-01-01','1970-01-01',2),(6,'1970-01-01','1970-01-01',3),(7,'1970-01-01','1970-01-01',1),(8,'1970-01-01','1970-01-01',2),(9,'1970-01-01','1970-01-01',3),(10,'1970-01-01','1970-01-01',1),(11,'1970-01-01','1970-01-01',2),(12,'1970-01-01','1970-01-01',3),(13,'1970-01-01','1970-01-01',1),(14,'1970-01-01','1970-01-01',2),(15,'1970-01-01','1970-01-01',3),(16,'1970-01-01','1970-01-01',1),(17,'1970-01-01','1970-01-01',2),(18,'1970-01-01','1970-01-01',3),(19,'1970-01-01','1970-01-01',1),(20,'1970-01-01','1970-01-01',2),(21,'1970-01-01','1970-01-01',3),(22,'1970-01-01','1970-01-01',1),(23,'1970-01-01','1970-01-01',2),(24,'1970-01-01','1970-01-01',3),(25,'1970-01-01','1970-01-01',1),(26,'1970-01-01','1970-01-01',2),(27,'1970-01-01','1970-01-01',3),(28,'1970-01-01','1970-01-01',1),(29,'1970-01-01','1970-01-01',2),(30,'1970-01-01','1970-01-01',3),(31,'1970-01-01','1970-01-01',1),(32,'1970-01-01','1970-01-01',2),(33,'1970-01-01','1970-01-01',3),(34,'1970-01-01','1970-01-01',1),(35,'1970-01-01','1970-01-01',2),(36,'1970-01-01','1970-01-01',3),(37,'1970-01-01','1970-01-01',1),(38,'1970-01-01','1970-01-01',2),(39,'1970-01-01','1970-01-01',3),(40,'1970-01-01','1970-01-01',1),(41,'1970-01-01','1970-01-01',2),(42,'1970-01-01','1970-01-01',3),(43,'1970-01-01','1970-01-01',1),(44,'1970-01-01','1970-01-01',2),(45,'1970-01-01','1970-01-01',3),(46,'1970-01-01','1970-01-01',1),(47,'1970-01-01','1970-01-01',2),(48,'1970-01-01','1970-01-01',3),(49,'1970-01-01','1970-01-01',1),(50,'1970-01-01','1970-01-01',2),(51,'1970-01-01','1970-01-01',3),(52,'1970-01-01','1970-01-01',1),(53,'1970-01-01','1970-01-01',2),(54,'1970-01-01','1970-01-01',3),(55,'1970-01-01','1970-01-01',1),(56,'1970-01-01','1970-01-01',2),(57,'1970-01-01','1970-01-01',3),(58,'1970-01-01','1970-01-01',1),(59,'1970-01-01','1970-01-01',2),(60,'1970-01-01','1970-01-01',3),(61,'1970-01-01','1970-01-01',1),(62,'1970-01-01','1970-01-01',2),(63,'1970-01-01','1970-01-01',3),(64,'1970-01-01','1970-01-01',1),(65,'1970-01-01','1970-01-01',2),(66,'1970-01-01','1970-01-01',3),(67,'1970-01-01','1970-01-01',1),(68,'1970-01-01','1970-01-01',2),(69,'1970-01-01','1970-01-01',3),(70,'1970-01-01','1970-01-01',1),(71,'1970-01-01','1970-01-01',2),(72,'1970-01-01','1970-01-01',3),(73,'1970-01-01','1970-01-01',1),(74,'1970-01-01','1970-01-01',2),(75,'1970-01-01','1970-01-01',3),(76,'1970-01-01','1970-01-01',1),(77,'1970-01-01','1970-01-01',2),(78,'1970-01-01','1970-01-01',3),(79,'1970-01-01','1970-01-01',1),(80,'1970-01-01','1970-01-01',2),(81,'1970-01-01','1970-01-01',3),(82,'1970-01-01','1970-01-01',1),(83,'1970-01-01','1970-01-01',2),(84,'1970-01-01','1970-01-01',3),(85,'1970-01-01','1970-01-01',1),(86,'1970-01-01','1970-01-01',2),(87,'1970-01-01','1970-01-01',3),(88,'1970-01-01','1970-01-01',1),(89,'1970-01-01','1970-01-01',2),(90,'1970-01-01','1970-01-01',3),(91,'1970-01-01','1970-01-01',1),(92,'1970-01-01','1970-01-01',2),(93,'1970-01-01','1970-01-01',3),(94,'1970-01-01','1970-01-01',1),(95,'1970-01-01','1970-01-01',2),(96,'1970-01-01','1970-01-01',3),(97,'1970-01-01','1970-01-01',1),(98,'1970-01-01','1970-01-01',2),(99,'1970-01-01','1970-01-01',3),(100,'1970-01-01','1970-01-01',1);
/*!40000 ALTER TABLE `deliveries_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departments`
--

DROP TABLE IF EXISTS `departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `departments` (
  `department_id` int(11) NOT NULL AUTO_INCREMENT,
  `department_name` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departments`
--

LOCK TABLES `departments` WRITE;
/*!40000 ALTER TABLE `departments` DISABLE KEYS */;
INSERT INTO `departments` VALUES (1,'Executives'),(2,'Finance'),(3,'Marketing'),(4,'Production'),(5,'Distribution');
/*!40000 ALTER TABLE `departments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee` (
  `personnel_id` int(11) NOT NULL AUTO_INCREMENT,
  `f_name` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `l_name` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `department_id` int(11) NOT NULL,
  PRIMARY KEY (`personnel_id`),
  KEY `fk_departments` (`department_id`),
  CONSTRAINT `fk_departments` FOREIGN KEY (`department_id`) REFERENCES `departments` (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'Stan','Bacchus',1),(2,'Davis','Bacchus',1),(3,'Janet','Collins',2),(4,'Roz','Murphy',3),(5,'Bob','Ulrich',3),(6,'Henry','Doyle',4),(7,'Maria','Costanza',5);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_time`
--

DROP TABLE IF EXISTS `employee_time`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee_time` (
  `record_id` int(11) NOT NULL AUTO_INCREMENT,
  `personnel_id` int(11) NOT NULL,
  `work_date` date DEFAULT NULL,
  `hours` int(11) DEFAULT NULL,
  PRIMARY KEY (`record_id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_time`
--

LOCK TABLES `employee_time` WRITE;
/*!40000 ALTER TABLE `employee_time` DISABLE KEYS */;
INSERT INTO `employee_time` VALUES (1,0,'1999-06-21',16),(2,0,'1992-06-27',0),(3,0,'2000-03-27',16),(4,0,'2012-12-11',0),(5,0,'1988-07-16',1),(6,0,'1994-10-01',15),(7,0,'2001-06-26',18),(8,0,'1997-01-21',15),(9,0,'1975-04-07',7),(10,0,'1996-02-15',10),(11,0,'1990-08-19',21),(12,0,'1986-02-28',23),(13,0,'1995-08-27',1),(14,0,'1973-12-14',11),(15,0,'1991-04-09',5),(16,0,'1988-03-01',16),(17,0,'2006-07-24',12),(18,0,'1999-07-16',13),(19,0,'2007-08-17',7),(20,0,'1988-04-04',3),(21,0,'2011-05-28',3),(22,0,'1978-05-13',22),(23,0,'2007-10-12',3),(24,0,'1974-01-11',2),(25,0,'1988-04-16',6),(26,0,'1987-08-23',21),(27,0,'1973-05-19',9),(28,0,'2010-05-26',2),(29,0,'2019-01-03',14),(30,0,'2000-05-14',20),(31,0,'1985-09-03',16),(32,0,'2004-01-16',18),(33,0,'2009-07-29',5),(34,0,'2000-03-18',14),(35,0,'2017-03-04',13),(36,0,'2020-07-03',8),(37,0,'1979-01-22',2),(38,0,'1981-12-30',15),(39,0,'2004-12-17',23),(40,0,'2015-03-30',6),(41,0,'1999-08-05',22),(42,0,'2019-09-09',23),(43,0,'2014-05-30',11),(44,0,'2008-12-08',14),(45,0,'1993-09-18',9),(46,0,'2013-04-22',7),(47,0,'2002-10-16',1),(48,0,'1975-12-26',17),(49,0,'2022-01-19',9),(50,0,'2008-06-19',20);
/*!40000 ALTER TABLE `employee_time` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suppliers`
--

DROP TABLE IF EXISTS `suppliers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `suppliers` (
  `supplier_id` int(11) NOT NULL AUTO_INCREMENT,
  `supplier_name` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `supplier_address` varchar(60) COLLATE utf8mb4_unicode_ci NOT NULL,
  `supplier_contact` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`supplier_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suppliers`
--

LOCK TABLES `suppliers` WRITE;
/*!40000 ALTER TABLE `suppliers` DISABLE KEYS */;
INSERT INTO `suppliers` VALUES (1,'XYZ Bottling','123 Seasame Street','Jim Morrison'),(2,'East Coast Paper Products','1601 Pennsylvania Avenue','Burt Macklin'),(3,'London Flow and Storage Solutions','221C Baker Street','James Potter');
/*!40000 ALTER TABLE `suppliers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplies`
--

DROP TABLE IF EXISTS `supplies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `supplies` (
  `item_id` int(11) NOT NULL AUTO_INCREMENT,
  `supply_name` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `supplier_id` int(11) NOT NULL,
  PRIMARY KEY (`item_id`),
  KEY `fk_suppliers` (`supplier_id`),
  CONSTRAINT `fk_suppliers` FOREIGN KEY (`supplier_id`) REFERENCES `suppliers` (`supplier_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplies`
--

LOCK TABLES `supplies` WRITE;
/*!40000 ALTER TABLE `supplies` DISABLE KEYS */;
INSERT INTO `supplies` VALUES (1,'Bottles',1),(2,'Corks',1),(3,'Labels',2),(4,'Boxes',2),(5,'Vats',3),(6,'Tubing',3);
/*!40000 ALTER TABLE `supplies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wine_distribution`
--

DROP TABLE IF EXISTS `wine_distribution`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `wine_distribution` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_date` date DEFAULT NULL,
  `wine_name` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `order_units` int(11) NOT NULL,
  `distributor_name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wine_distribution`
--

LOCK TABLES `wine_distribution` WRITE;
/*!40000 ALTER TABLE `wine_distribution` DISABLE KEYS */;
INSERT INTO `wine_distribution` VALUES (1,'1970-01-01','Cabernet',0,'Abernathy, Weber and Bauch'),(2,'1970-01-01','Chardonnay',0,'O\'Hara, Bartoletti and Wehner'),(3,'1970-01-01','Merlot',0,'Maggio Group'),(4,'1970-01-01','Cabernet',0,'Lebsack Group'),(5,'1970-01-01','Chardonnay',0,'Veum and Sons'),(6,'1970-01-01','Merlot',0,'Bashirian-Jacobi'),(7,'1970-01-01','Cabernet',0,'Harber, Mohr and Cole'),(8,'1970-01-01','Chardonnay',0,'Shanahan, Kuphal and Kreiger'),(9,'1970-01-01','Merlot',0,'Bins and Sons'),(10,'1970-01-01','Cabernet',0,'Fay-Hammes'),(11,'1970-01-01','Chardonnay',0,'Lang-Kuhn'),(12,'1970-01-01','Merlot',0,'Emard, Olson and Nikolaus'),(13,'1970-01-01','Cabernet',0,'Raynor, Rempel and Hauck'),(14,'1970-01-01','Chardonnay',0,'Nader-Hamill'),(15,'1970-01-01','Merlot',0,'Ritchie Ltd'),(16,'1970-01-01','Cabernet',0,'Goldner-Nikolaus'),(17,'1970-01-01','Chardonnay',0,'Gusikowski-Kuhic'),(18,'1970-01-01','Merlot',0,'Bergstrom-DuBuque'),(19,'1970-01-01','Cabernet',0,'Zemlak-Herman'),(20,'1970-01-01','Chardonnay',0,'Kovacek, Nikolaus and Klocko'),(21,'1970-01-01','Merlot',0,'Bode, Windler and Muller'),(22,'1970-01-01','Cabernet',0,'Sporer Inc'),(23,'1970-01-01','Chardonnay',0,'Reichel LLC'),(24,'1970-01-01','Merlot',0,'O\'Conner, Murazik and Langworth'),(25,'1970-01-01','Cabernet',0,'Swaniawski Ltd'),(26,'1970-01-01','Chardonnay',0,'Watsica and Sons'),(27,'1970-01-01','Merlot',0,'Yundt, Harber and Hintz'),(28,'1970-01-01','Cabernet',0,'Hintz and Sons'),(29,'1970-01-01','Chardonnay',0,'Collins and Sons'),(30,'1970-01-01','Merlot',0,'DuBuque PLC'),(31,'1970-01-01','Cabernet',0,'Nader Ltd'),(32,'1970-01-01','Chardonnay',0,'Ebert, Tillman and Romaguera'),(33,'1970-01-01','Merlot',0,'Stroman, Abbott and Mitchell'),(34,'1970-01-01','Cabernet',0,'Bechtelar-Glover'),(35,'1970-01-01','Chardonnay',0,'Beier, Simonis and Zboncak'),(36,'1970-01-01','Merlot',0,'Pfannerstill, Jaskolski and Hagenes'),(37,'1970-01-01','Cabernet',0,'Klein-Witting'),(38,'1970-01-01','Chardonnay',0,'Cormier, Bednar and Franecki'),(39,'1970-01-01','Merlot',0,'Brakus-Gleason'),(40,'1970-01-01','Cabernet',0,'Medhurst, Dooley and O\'Hara'),(41,'1970-01-01','Chardonnay',0,'McCullough-Bergstrom'),(42,'1970-01-01','Merlot',0,'Gerhold-Abbott'),(43,'1970-01-01','Cabernet',0,'Shanahan Inc'),(44,'1970-01-01','Chardonnay',0,'Rau, Moen and Bins'),(45,'1970-01-01','Merlot',0,'Farrell Ltd'),(46,'1970-01-01','Cabernet',0,'Schiller-Bartoletti'),(47,'1970-01-01','Chardonnay',0,'Friesen Group'),(48,'1970-01-01','Merlot',0,'McKenzie-Conroy'),(49,'1970-01-01','Cabernet',0,'Nader-Harber'),(50,'1970-01-01','Chardonnay',0,'Grimes-Boehm'),(51,'1970-01-01','Merlot',0,'Swaniawski, McKenzie and Schuppe'),(52,'1970-01-01','Cabernet',0,'Feeney-Feeney'),(53,'1970-01-01','Chardonnay',0,'Rempel LLC'),(54,'1970-01-01','Merlot',0,'Witting-Bins'),(55,'1970-01-01','Cabernet',0,'Yundt, Larkin and Mante'),(56,'1970-01-01','Chardonnay',0,'Rutherford, Cummerata and Hoeger'),(57,'1970-01-01','Merlot',0,'Shanahan-Gutmann'),(58,'1970-01-01','Cabernet',0,'McLaughlin-Waelchi'),(59,'1970-01-01','Chardonnay',0,'Lang-Donnelly'),(60,'1970-01-01','Merlot',0,'Barton, Beer and Hammes'),(61,'1970-01-01','Cabernet',0,'Beier Group'),(62,'1970-01-01','Chardonnay',0,'Zieme, Boyer and Murphy'),(63,'1970-01-01','Merlot',0,'Kutch and Sons'),(64,'1970-01-01','Cabernet',0,'DuBuque, Huel and Rolfson'),(65,'1970-01-01','Chardonnay',0,'Morissette, Cummings and Lebsack'),(66,'1970-01-01','Merlot',0,'Hilpert LLC'),(67,'1970-01-01','Cabernet',0,'Vandervort-Swift'),(68,'1970-01-01','Chardonnay',0,'Doyle Group'),(69,'1970-01-01','Merlot',0,'Auer-O\'Conner'),(70,'1970-01-01','Cabernet',0,'Howell-Kling'),(71,'1970-01-01','Chardonnay',0,'Nicolas Inc'),(72,'1970-01-01','Merlot',0,'Lind, Torphy and Cummings'),(73,'1970-01-01','Cabernet',0,'Smitham, Lubowitz and Crona'),(74,'1970-01-01','Chardonnay',0,'Considine PLC'),(75,'1970-01-01','Merlot',0,'Gusikowski Ltd'),(76,'1970-01-01','Cabernet',0,'Mraz, Auer and Vandervort'),(77,'1970-01-01','Chardonnay',0,'Armstrong Ltd'),(78,'1970-01-01','Merlot',0,'Mraz-Beatty'),(79,'1970-01-01','Cabernet',0,'Pacocha-Schiller'),(80,'1970-01-01','Chardonnay',0,'Altenwerth-Wisozk'),(81,'1970-01-01','Merlot',0,'Kub-Hessel'),(82,'1970-01-01','Cabernet',0,'Zieme, Carter and Padberg'),(83,'1970-01-01','Chardonnay',0,'Ziemann, Hauck and Boehm'),(84,'1970-01-01','Merlot',0,'Rippin, Weissnat and O\'Reilly'),(85,'1970-01-01','Cabernet',0,'Cremin Ltd'),(86,'1970-01-01','Chardonnay',0,'Reynolds, Hoeger and Kub'),(87,'1970-01-01','Merlot',0,'Prosacco Ltd'),(88,'1970-01-01','Cabernet',0,'Tillman, Nitzsche and Gusikowski'),(89,'1970-01-01','Chardonnay',0,'Hartmann LLC'),(90,'1970-01-01','Merlot',0,'Grant, Ruecker and Auer'),(91,'1970-01-01','Cabernet',0,'Larkin-Lind'),(92,'1970-01-01','Chardonnay',0,'Hartmann and Sons'),(93,'1970-01-01','Merlot',0,'Abernathy-Sauer'),(94,'1970-01-01','Cabernet',0,'Rippin-Dietrich'),(95,'1970-01-01','Chardonnay',0,'Blick Group'),(96,'1970-01-01','Merlot',0,'Conn, Zulauf and Schmitt'),(97,'1970-01-01','Cabernet',0,'Zulauf-Ebert'),(98,'1970-01-01','Chardonnay',0,'Anderson, Dicki and Bruen'),(99,'1970-01-01','Merlot',0,'Ritchie-Gerhold'),(100,'1970-01-01','Cabernet',0,'Effertz Group');
/*!40000 ALTER TABLE `wine_distribution` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wine_production`
--

DROP TABLE IF EXISTS `wine_production`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `wine_production` (
  `batch_id` int(11) NOT NULL AUTO_INCREMENT,
  `wine_name` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `born_date` date DEFAULT NULL,
  `units_produced` int(11) DEFAULT NULL,
  PRIMARY KEY (`batch_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wine_production`
--

LOCK TABLES `wine_production` WRITE;
/*!40000 ALTER TABLE `wine_production` DISABLE KEYS */;
INSERT INTO `wine_production` VALUES (1,'Cabernet','2022-07-10',664),(2,'Chardonnay','2022-07-10',775),(3,'Merlot','2022-07-10',497);
/*!40000 ALTER TABLE `wine_production` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-14  6:24:24
