-- MySQL dump 10.13  Distrib 5.1.65, for unknown-linux-gnu (x86_64)
--
-- Host: localhost    Database: notes
-- ------------------------------------------------------
-- Server version	5.1.65-LTOPS-log

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
-- Table structure for table `comment`
--

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES (1,1,'2012-09-03 16:11:59','秦汉唐宋元','保密','不错'),(2,5,'2012-09-10 14:07:34','丫头','731486609@qq.com','左哥威武 啊哈哈哈'),(3,6,'2012-09-10 14:08:01','丫头','啊哈哈哈','啊哈哈哈哈啊哈哈哈');
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notes`
--

-- Dumping data for table `notes`
--

LOCK TABLES `notes` WRITE;
/*!40000 ALTER TABLE `notes` DISABLE KEYS */;
INSERT INTO `notes` VALUES (1,'2012-09-03','15:24:40','hello world!',1),(2,'2012-09-03','18:03:29','test 1',0),(3,'2012-09-04','18:02:58','first uwsgi',0),(4,'2012-09-05','17:32:49',' limit_conn one 20;          //连接数限制  \r\n limit_rate 500k;            //带宽限制  ',0),(5,'2012-09-07','22:08:45','lastb 登录失败的记录',1),(6,'2012-09-10','13:01:16','mysql查询表结构 desc',1),(7,'2012-09-10','13:01:42','删除空目录\r\nfind . -type d -empty |xargs rm -rf',0),(8,'2012-09-30','19:06:44','中秋快乐',0),(9,'2012-10-18','15:43:53','库巴 第二天 ！',0);
/*!40000 ALTER TABLE `notes` ENABLE KEYS */;
UNLOCK TABLES;

