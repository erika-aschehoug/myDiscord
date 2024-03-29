-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: db_discord
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `chat_room`
--

DROP TABLE IF EXISTS `chat_room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chat_room` (
  `id_chat_room` int NOT NULL AUTO_INCREMENT,
  `room_name` varchar(255) DEFAULT NULL,
  `canal_type` varchar(255) DEFAULT NULL,
  `private` tinyint(1) DEFAULT NULL,
  `public` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id_chat_room`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chat_room`
--

LOCK TABLES `chat_room` WRITE;
/*!40000 ALTER TABLE `chat_room` DISABLE KEYS */;
/*!40000 ALTER TABLE `chat_room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notification`
--

DROP TABLE IF EXISTS `notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notification` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `channel_id` int DEFAULT NULL,
  `messages_counter` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notification`
--

LOCK TABLES `notification` WRITE;
/*!40000 ALTER TABLE `notification` DISABLE KEYS */;
INSERT INTO `notification` VALUES (1,2,1,3),(2,3,1,5),(3,4,1,0);
/*!40000 ALTER TABLE `notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permissions`
--

DROP TABLE IF EXISTS `permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_affiliate_user` int DEFAULT NULL,
  `id_affiliate_canal` int DEFAULT NULL,
  `admin` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permissions`
--

LOCK TABLES `permissions` WRITE;
/*!40000 ALTER TABLE `permissions` DISABLE KEYS */;
INSERT INTO `permissions` VALUES (1,2,2,1);
/*!40000 ALTER TABLE `permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `posts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `body` text,
  `user_id` int DEFAULT NULL,
  `id_affiliate_chanel` int DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `connection` tinyint(1) DEFAULT NULL,
  `disconnection` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
INSERT INTO `posts` VALUES (1,'Jusan Boris s\'est connect├® au chat',2,1,'2024-03-01 14:04:47',1,0),(2,'Jusan Boris s\'est d├®connect├® du chat',2,1,'2024-03-01 14:05:05',0,1),(3,'Jusan Boris s\'est connect├® au chat',2,1,'2024-03-01 14:05:08',1,0),(4,'Jusan Boris s\'est d├®connect├® du chat',2,1,'2024-03-01 14:05:11',0,1),(5,'Hugo Esquer s\'est connect├® au chat',3,1,'2024-03-01 16:44:51',1,0),(6,'Hugo Esquer s\'est d├®connect├® du chat',3,1,'2024-03-01 16:44:53',0,1),(7,'Hugo Esquer s\'est connect├® au chat',3,2,'2024-03-01 16:44:54',1,0),(8,'Hugo Esquer s\'est d├®connect├® du chat',3,2,'2024-03-01 16:45:09',0,1),(9,'Jusan Boris s\'est connect├® au chat',2,2,'2024-03-01 16:53:23',1,0),(10,'Jusan Boris s\'est connect├® au chat',2,2,'2024-03-01 16:54:20',1,0),(11,'Jusan Boris s\'est connect├® au chat',2,2,'2024-03-01 17:13:39',1,0),(12,'Jusan Boris s\'est connect├® au chat',2,2,'2024-03-01 17:14:49',1,0),(13,'Jusan Boris s\'est connect├® au chat',2,2,'2024-03-01 17:18:37',1,0),(14,'Jusan Boris s\'est connect├® au chat',2,2,'2024-03-01 17:21:32',1,0),(15,'Jusan Boris s\'est connect├® au chat',2,2,'2024-03-01 17:25:16',1,0),(16,'Jusan Boris s\'est d├®connect├® du chat',2,2,'2024-03-01 17:25:41',0,1),(17,'Jusan Boris s\'est connect├® au chat',2,2,'2024-03-01 17:27:07',1,0),(18,'Jusan Boris s\'est d├®connect├® du chat',2,2,'2024-03-01 17:27:25',0,1),(19,'Pierre Mazard s\'est connect├® au chat',4,2,'2024-03-01 17:27:36',1,0),(20,'Jusan Boris s\'est connect├® au chat',2,2,'2024-03-01 17:37:29',1,0),(21,'Jusan Boris s\'est connect├® au chat',2,2,'2024-03-01 17:39:32',1,0),(22,'Jusan Boris s\'est connect├® au chat',2,2,'2024-03-01 17:42:12',1,0),(23,'Jusan Boris s\'est connect├® au chat',2,2,'2024-03-01 17:45:30',1,0),(24,'Jusan Boris s\'est connect├® au chat',2,2,'2024-03-01 17:47:18',1,0),(25,'Jusan Boris s\'est connect├® au chat',2,2,'2024-03-01 17:48:54',1,0),(26,'Jusan Boris s\'est connect├® au chat',2,2,'2024-03-01 17:50:30',1,0),(27,'Jusan Boris s\'est connect├® au chat',2,2,'2024-03-01 17:51:50',1,0),(28,'Jusan Boris s\'est connect├® au chat',2,2,'2024-03-01 17:56:24',1,0);
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reaction`
--

DROP TABLE IF EXISTS `reaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reaction` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_affiliate_post` int DEFAULT NULL,
  `id_affiliate_user` int DEFAULT NULL,
  `emoji_type` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reaction`
--

LOCK TABLES `reaction` WRITE;
/*!40000 ALTER TABLE `reaction` DISABLE KEYS */;
/*!40000 ALTER TABLE `reaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `user_first_name` varchar(255) DEFAULT NULL,
  `mail` varchar(255) DEFAULT NULL,
  `passwd` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (2,'Boris','Jusan','bj@gmail.com','26adf3b164ff3580aac000a73837115f1fb6c6a440d871ceaf3f3ec58c1219d1'),(3,'Esquer','Hugo','123','a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),(4,'Mazard','Pierre','PM','03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-01 20:01:27
