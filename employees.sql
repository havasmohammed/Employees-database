-- MySQL dump 10.13  Distrib 5.5.43, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: Employees
-- ------------------------------------------------------
-- Server version	5.5.43-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `basic_details`
--

DROP TABLE IF EXISTS `basic_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `basic_details` (
  `empno` int(11) NOT NULL DEFAULT '0',
  `name` varchar(30) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `designationid` int(11) DEFAULT NULL,
  `salary` int(11) DEFAULT NULL,
  PRIMARY KEY (`empno`),
  KEY `designationid` (`designationid`),
  CONSTRAINT `basic_details_ibfk_1` FOREIGN KEY (`designationid`) REFERENCES `designation_details` (`designationid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `basic_details`
--

LOCK TABLES `basic_details` WRITE;
/*!40000 ALTER TABLE `basic_details` DISABLE KEYS */;
INSERT INTO `basic_details` VALUES (101,'Arun',28,441,25000),(102,'Anu',23,442,15000),(103,'Anand',29,443,27000),(104,'Jax',32,444,35000),(105,'Navas',39,445,50000),(106,'Issac',30,446,30000),(109,'Amer',29,442,15000),(110,'Hari',36,446,35000),(112,'Manu',28,446,35000),(113,'Yash',31,446,35000),(114,'Nandu',34,444,40000);
/*!40000 ALTER TABLE `basic_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `daily_activities`
--

DROP TABLE IF EXISTS `daily_activities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `daily_activities` (
  `designationid` int(11) NOT NULL DEFAULT '0',
  `date` date DEFAULT NULL,
  `project` varchar(30) DEFAULT NULL,
  `type` varchar(30) DEFAULT NULL,
  `description` varchar(30) DEFAULT NULL,
  `timespent` int(11) DEFAULT NULL,
  PRIMARY KEY (`designationid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `daily_activities`
--

LOCK TABLES `daily_activities` WRITE;
/*!40000 ALTER TABLE `daily_activities` DISABLE KEYS */;
INSERT INTO `daily_activities` VALUES (441,'2015-07-07','Network solutions','coding','ccchhh',8),(442,'2015-07-07','NA','training','python',8),(443,'2015-07-07','Like that ios app','webframe','aaddaawe',8),(444,'2015-07-07','Network solutions','development','aassvv',8),(445,'2015-07-07','Network solutions','management','akkhh',8),(446,'2015-07-07','Recruitment','offcampus','llksmm',8);
/*!40000 ALTER TABLE `daily_activities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department_details`
--

DROP TABLE IF EXISTS `department_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `department_details` (
  `designationid` int(11) NOT NULL DEFAULT '0',
  `department` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`designationid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department_details`
--

LOCK TABLES `department_details` WRITE;
/*!40000 ALTER TABLE `department_details` DISABLE KEYS */;
INSERT INTO `department_details` VALUES (441,'Python'),(442,'Python'),(443,'Java'),(444,'Reactjs'),(445,'Python'),(446,'Recruitment');
/*!40000 ALTER TABLE `department_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `designation_details`
--

DROP TABLE IF EXISTS `designation_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `designation_details` (
  `designationid` int(11) NOT NULL DEFAULT '0',
  `designation` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`designationid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `designation_details`
--

LOCK TABLES `designation_details` WRITE;
/*!40000 ALTER TABLE `designation_details` DISABLE KEYS */;
INSERT INTO `designation_details` VALUES (441,'Developer'),(442,'Intern'),(443,'Developer'),(444,'Team lead'),(445,'Project manager'),(446,'HR');
/*!40000 ALTER TABLE `designation_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `experience_Details`
--

DROP TABLE IF EXISTS `experience_Details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `experience_Details` (
  `designationid` int(11) NOT NULL DEFAULT '0',
  `level` int(11) DEFAULT NULL,
  PRIMARY KEY (`designationid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `experience_Details`
--

LOCK TABLES `experience_Details` WRITE;
/*!40000 ALTER TABLE `experience_Details` DISABLE KEYS */;
INSERT INTO `experience_Details` VALUES (441,2),(442,0),(443,2),(444,3),(445,4),(446,3);
/*!40000 ALTER TABLE `experience_Details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `qualification_details`
--

DROP TABLE IF EXISTS `qualification_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `qualification_details` (
  `designationid` int(11) NOT NULL DEFAULT '0',
  `qualification` varchar(30) DEFAULT NULL,
  `branch` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`designationid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qualification_details`
--

LOCK TABLES `qualification_details` WRITE;
/*!40000 ALTER TABLE `qualification_details` DISABLE KEYS */;
INSERT INTO `qualification_details` VALUES (441,'Btech','cs'),(442,'Btech','ec'),(443,'Btech','ec'),(444,'Btech','cs'),(445,'Btech mba','cs'),(446,'Mba','HR');
/*!40000 ALTER TABLE `qualification_details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-07-13 12:13:40
