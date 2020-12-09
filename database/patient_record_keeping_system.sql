-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: patient_record_keeping_system
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `patient_detail`
--

DROP TABLE IF EXISTS `patient_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient_detail` (
  `patient_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `age` int NOT NULL,
  `email` varchar(50) NOT NULL,
  `contact` varchar(10) NOT NULL,
  `gender` varchar(15) NOT NULL,
  `dep` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  PRIMARY KEY (`patient_id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_detail`
--

LOCK TABLES `patient_detail` WRITE;
/*!40000 ALTER TABLE `patient_detail` DISABLE KEYS */;
INSERT INTO `patient_detail` VALUES (5,'Nishma',19,'nishma@gmail.com','1234567890','female','Emergency','Butwal'),(6,'Nishma',19,'nishma@gmail.com','1234567890','female','Emergency','Butwal'),(7,'Nishma',19,'nishma@gmail.com','1234567890','female','Emergency','Butwal'),(8,'Nishma',19,'nishma@gmail.com','1234567890','female','Emergency','Butwal'),(9,'Nishma',19,'nishma@gmail.com','1234567890','female','Emergency','Butwal'),(10,'Nishma',19,'nishma@gmail.com','1234567890','female','Emergency','Butwal'),(11,'Nishma',19,'nishma@gmail.com','1234567890','female','Emergency','Butwal'),(12,'Nishma',19,'nishma@gmail.com','1234567890','female','Emergency','Butwal'),(13,'Nishma',19,'nishma@gmail.com','1234567890','female','Emergency','Butwal'),(14,'Nishma',19,'nishma@gmail.com','1234567890','female','Emergency','Butwal'),(15,'Nishma',19,'nishma@gmail.com','1234567890','female','Emergency','Butwal'),(16,'Nishma',19,'nishma@gmail.com','1234567890','female','Emergency','Butwal'),(17,'Nishma',19,'nishma@gmail.com','1234567890','female','Emergency','Butwal'),(18,'Nishma',19,'nishma@gmail.com','1234567890','female','Emergency','Butwal'),(19,'Nishmaf',19,'nishma@gmail.com','1234567890','Male','Emergency','Butwal\n'),(20,'Nishma',19,'nishma@gmail.com','1234567890','female','Emergency','Butwal'),(21,'Nishma',19,'nishma@gmail.com','1234567890','Male','Emergency','Butwal\n\n'),(29,'Nishma',19,'nishma@gmail.com','1234567890','Male','Emergency','Butwal\n\n\n'),(30,'ram',19,'nishma@gmail.com','1234567890','Male','Emergency','Butwal\n\n\n');
/*!40000 ALTER TABLE `patient_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registration`
--

DROP TABLE IF EXISTS `registration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registration` (
  `username` varchar(40) NOT NULL,
  `password` varchar(40) NOT NULL,
  `type` varchar(20) NOT NULL DEFAULT 'user',
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registration`
--

LOCK TABLES `registration` WRITE;
/*!40000 ALTER TABLE `registration` DISABLE KEYS */;
INSERT INTO `registration` VALUES ('Grandy','Hospital','user'),('Nishma','Upadhaya','admin');
/*!40000 ALTER TABLE `registration` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-07 18:00:45
