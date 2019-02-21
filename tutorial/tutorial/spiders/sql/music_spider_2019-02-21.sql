# ************************************************************
# Sequel Pro SQL dump
# Version 4096
#
# http://www.sequelpro.com/
# http://code.google.com/p/sequel-pro/
#
# Host: 172.28.39.183 (MySQL 5.7.22)
# Database: music_spider
# Generation Time: 2019-02-21 08:21:53 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table music_class
# ------------------------------------------------------------

DROP TABLE IF EXISTS `music_class`;

CREATE TABLE `music_class` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `class` varchar(255) DEFAULT '""',
  `subclass` varchar(255) DEFAULT '""',
  `artname` varchar(255) DEFAULT '""',
  `title` varchar(255) DEFAULT '""',
  `date` varchar(255) DEFAULT '""',
  `subclass_url` varchar(255) DEFAULT '""',
  `item_url` varchar(255) DEFAULT '""',
  `pdf_url` varchar(255) DEFAULT '""',
  `mp3_url` varchar(255) DEFAULT '""',
  `flag` int(1) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table music_item
# ------------------------------------------------------------

DROP TABLE IF EXISTS `music_item`;

CREATE TABLE `music_item` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `class` varchar(255) DEFAULT '""',
  `subclass` varchar(255) DEFAULT '""',
  `artname` varchar(255) DEFAULT '""',
  `title` varchar(255) DEFAULT '""',
  `date` varchar(255) DEFAULT '""',
  `subclass_url` varchar(255) DEFAULT '""',
  `item_url` varchar(255) DEFAULT '""',
  `pdf_url` varchar(255) NOT NULL DEFAULT '',
  `pdf_name` varchar(255) DEFAULT '""',
  `mp3_url` varchar(255) DEFAULT '""',
  `mp3_name` varchar(255) DEFAULT '""',
  `flag` int(1) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
