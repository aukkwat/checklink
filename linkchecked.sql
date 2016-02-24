/*
 Navicat Premium Data Transfer

 Source Server         : Checklink
 Source Server Type    : MySQL
 Source Server Version : 50543
 Source Host           : docker
 Source Database       : checklink

 Target Server Type    : MySQL
 Target Server Version : 50543
 File Encoding         : utf-8

 Date: 02/24/2016 14:34:49 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `linkchecked`
-- ----------------------------
DROP TABLE IF EXISTS `linkchecked`;
CREATE TABLE `linkchecked` (
  `datecheck` datetime DEFAULT NULL,
  `urlcheck` varchar(255) DEFAULT NULL,
  `statuscheck` int(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

SET FOREIGN_KEY_CHECKS = 1;
