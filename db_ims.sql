/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 10.4.8-MariaDB-log : Database - db_ims
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`db_ims` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `db_ims`;

/*Table structure for table `tb_pertandingan` */

DROP TABLE IF EXISTS `tb_pertandingan`;

CREATE TABLE `tb_pertandingan` (
  `id_pertandingan` int(11) NOT NULL AUTO_INCREMENT,
  `id_peserta_a` int(11) NOT NULL,
  `id_peserta_b` int(11) NOT NULL,
  `hasil` varchar(20) DEFAULT NULL,
  `mulai` varchar(20) DEFAULT NULL,
  `selesai` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_pertandingan`),
  KEY `id_peserta_a` (`id_peserta_a`),
  KEY `id_peserta_b` (`id_peserta_b`),
  CONSTRAINT `tb_pertandingan_ibfk_1` FOREIGN KEY (`id_peserta_a`) REFERENCES `tb_peserta` (`id_peserta`),
  CONSTRAINT `tb_pertandingan_ibfk_2` FOREIGN KEY (`id_peserta_b`) REFERENCES `tb_peserta` (`id_peserta`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tb_pertandingan` */

insert  into `tb_pertandingan`(`id_pertandingan`,`id_peserta_a`,`id_peserta_b`,`hasil`,`mulai`,`selesai`) values (2,1,3,'2-1','17.00','17.10');

/*Table structure for table `tb_peserta` */

DROP TABLE IF EXISTS `tb_peserta`;

CREATE TABLE `tb_peserta` (
  `id_peserta` int(11) NOT NULL AUTO_INCREMENT,
  `id_rank` int(11) NOT NULL,
  `nama_depan` varchar(30) DEFAULT NULL,
  `nama_belakang` varchar(30) DEFAULT NULL,
  `alamat` varchar(30) DEFAULT NULL,
  `no_telp` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`id_peserta`),
  KEY `id_rank` (`id_rank`),
  CONSTRAINT `tb_peserta_ibfk_1` FOREIGN KEY (`id_rank`) REFERENCES `tb_rank` (`id_rank`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tb_peserta` */

insert  into `tb_peserta`(`id_peserta`,`id_rank`,`nama_depan`,`nama_belakang`,`alamat`,`no_telp`) values (1,1,'cahya','wibawa','bali','081'),(3,2,'JAYA','BHASWARA','BALI','082');

/*Table structure for table `tb_rank` */

DROP TABLE IF EXISTS `tb_rank`;

CREATE TABLE `tb_rank` (
  `id_rank` int(11) NOT NULL AUTO_INCREMENT,
  `rank` varchar(50) DEFAULT NULL,
  `deskripsi` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id_rank`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tb_rank` */

insert  into `tb_rank`(`id_rank`,`rank`,`deskripsi`) values (1,'master','pro player'),(2,'grandmaster','lebih pro diatas master'),(3,'pro','mtp');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
