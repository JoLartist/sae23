-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: May 05, 2024 at 08:30 PM
-- Server version: 8.2.0
-- PHP Version: 8.2.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rugby`
--
CREATE DATABASE IF NOT EXISTS `rugby` DEFAULT CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci;
USE `rugby`;

-- --------------------------------------------------------

--
-- Table structure for table `equipe`
--

DROP TABLE IF EXISTS `equipe`;
CREATE TABLE IF NOT EXISTS `equipe` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nom_equipe` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `equipe`
--

INSERT INTO `equipe` (`ID`, `Nom_equipe`) VALUES
(1, 'Agen'),
(2, 'Bayonne'),
(3, 'Bordeaux'),
(4, 'Brive'),
(5, 'Castres'),
(6, 'Clermont'),
(7, 'La Rochelle'),
(8, 'Lyon'),
(9, 'Montpellier'),
(10, 'Paris'),
(11, 'Pau'),
(12, 'Racing92'),
(13, 'Toulon'),
(14, 'Toulouse');

-- --------------------------------------------------------

--
-- Table structure for table `joueur`
--

DROP TABLE IF EXISTS `joueur`;
CREATE TABLE IF NOT EXISTS `joueur` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Nom` varchar(255) DEFAULT NULL,
  `Date_naissance` date DEFAULT NULL,
  `Poste_prefere` varchar(255) DEFAULT NULL,
  `ID_equipe` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `ID_equipe` (`ID_equipe`)
) ENGINE=InnoDB AUTO_INCREMENT=596 DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `joueur`
--

INSERT INTO `joueur` (`ID`, `Nom`, `Date_naissance`, `Poste_prefere`, `ID_equipe`) VALUES
(1, 'ANTON PEIKRISHVILI', '1987-09-18', 'Pilier', 1),
(2, 'DAVE RYAN', '1986-04-21', 'Pilier', 1),
(3, 'GIORGI TETRASHVILI', '1993-08-31', 'Pilier', 1),
(4, 'KAMALIELE TUFELE', '1995-10-11', 'Pilier', 1),
(5, 'MALINO VANAÏ', '1993-05-04', 'Pilier', 1),
(6, 'MORGAN PHÉLIPPONNEAU', '1989-09-05', 'Pilier', 1),
(7, 'WALTER DESMAISON', '1991-10-18', 'Pilier', 1),
(8, 'CLÉMENT MARTINEZ', '1996-03-14', 'Talonneur', 1),
(9, 'MARC BARTHOMEUF', '1991-07-19', 'Talonneur', 1),
(10, 'PAULA NGAUAMO', '1990-02-19', 'Talonneur', 1),
(11, 'ADRIAN MOTOC', '1996-07-11', '2ème ligne', 1),
(12, 'ANDRÉS ZAFRA', '1996-03-26', '2ème ligne', 1),
(13, 'MICKAËL DE MARCO', '1989-04-22', '2ème ligne', 1),
(14, 'PIERCE PHILLIPS', '1992-10-06', '2ème ligne', 1),
(15, 'TOM MURDAY', '1989-04-27', '2ème ligne', 1),
(16, 'DYLAN HAYES', '1994-02-11', '3ème ligne', 1),
(17, 'LAURENCE PEARCE', '1990-12-03', '3ème ligne', 1),
(18, 'ROMAIN BRIATTE', '1993-02-18', '3ème ligne', 1),
(19, 'VINCENT FARRÉ', '1990-06-06', '3ème ligne', 1),
(20, 'HUGO VERDU', '1996-10-24', 'Mêlée', 1),
(21, 'PAUL ABADIE', '1994-07-28', 'Mêlée', 1),
(22, 'XAVIER CHAUVEAU', '1992-10-14', 'Mêlée', 1),
(23, 'RAPHAËL LAGARDE', '1988-10-30', 'Ouverture', 1),
(24, 'ALBAN CONDUCHÉ', '1996-10-29', 'Centre', 1),
(25, 'JOHANN SADIE', '1989-01-23', 'Centre', 1),
(26, 'JORDAN PULETUA', '1990-02-28', 'Centre', 1),
(27, 'SAM VAKA', '1992-10-26', 'Centre', 1),
(28, 'BENITO MASILEVU', '1989-10-07', 'Ailier', 1),
(29, 'JULIEN JANÉ', '1989-09-12', 'Ailier', 1),
(30, 'TIMILAI ROKODURU', '1993-01-21', 'Ailier', 1),
(31, 'VALENTIN SAURS', '1995-02-12', 'Ailier', 1),
(32, 'JJ TAULAGI', '1993-06-18', 'Arrière', 1),
(33, 'LORIS TOLOT', '1993-03-03', 'Arrière', 1),
(34, 'MATHIEU LAMOULIE', '1990-08-07', 'Arrière', 1),
(35, 'ARETZ IGUINIZ', '1983-06-03', 'Pilier', 1),
(36, 'CENSUS JOHNSTON', '1981-05-06', 'Pilier', 2),
(37, 'JEAN-BAPTISTE DE CLERCQ', '1994-02-23', 'Pilier', 2),
(38, 'JON ZABALA', '1996-11-26', 'Pilier', 2),
(39, 'LUC MOUSSET', '1994-04-03', 'Pilier', 2),
(40, 'SWAN CORMENIER', '1996-01-10', 'Pilier', 2),
(41, 'TOMAAKINO TAUFA', '1995-03-09', 'Pilier', 2),
(42, 'UGO BONIFACE', '1998-07-21', 'Pilier', 2),
(43, 'VILIAMU AFATIA', '1990-05-24', 'Pilier', 2),
(44, 'MAXIME DELONCA', '1988-04-29', 'Talonneur', 2),
(45, 'MAXIME LAMOTHE', '1998-10-03', 'Talonneur', 2),
(46, 'TORSTEN VAN JAARSVELD', '1987-06-30', 'Talonneur', 2),
(47, 'ADAM JAULHAC', '1988-01-31', '2ème ligne', 2),
(48, 'BASTIEN BERGOUNIOUX', '1996-06-18', '2ème ligne', 2),
(49, 'EDWIN MAKA', '1993-01-25', '2ème ligne', 2),
(50, 'EVRARD DION OULAI', '1993-06-22', '2ème ligne', 2),
(51, 'GUILLAUME DUCAT', '1996-05-20', '2ème ligne', 2),
(52, 'MARIANO GALARZA', '1986-12-11', '2ème ligne', 2),
(53, 'PIETER JAN VAN LILL', '1983-12-04', '2ème ligne', 2),
(54, 'ANDRÉ GORIN', '1987-11-30', '3ème ligne', 2),
(55, 'ANTOINE BATTUT', '1984-01-01', '3ème ligne', 2),
(56, 'ARMANDT KOSTER', '1990-01-20', '3ème ligne', 2),
(57, 'ARNAUD DUPUTS', '1995-07-26', '3ème ligne', 2),
(58, 'BAPTISTE HÉGUY', '1998-05-11', '3ème ligne', 2),
(59, 'BENJAMIN COLLET', '1989-04-11', '3ème ligne', 2),
(60, 'FILIMO TAOFIFENUA', '1993-10-15', '3ème ligne', 2),
(61, 'JEAN MONRIBOT', '1987-10-11', '3ème ligne', 2),
(62, 'MAT LUAMANU', '1988-03-04', '3ème ligne', 2),
(63, 'TOM DARLET', '1996-08-06', '3ème ligne', 2),
(64, 'EMMANUEL SAUBUSSE', '1989-11-23', 'Mêlée', 2),
(65, 'GUILLAUME ROUET', '1988-08-13', 'Mêlée', 2),
(66, 'MICHAEL RURU', '1990-12-03', 'Mêlée', 2),
(67, 'BRANDON FAJARDO', '1994-06-25', 'Ouverture', 2),
(68, 'MANUEL ORDAS', '1998-02-21', 'Ouverture', 2),
(69, 'ALOFA ALOFA', '1991-03-12', 'Centre', 2),
(70, 'CALLUM WILSON', '1990-10-28', 'Centre', 2),
(71, 'MAILE MAMAO', '1996-01-07', 'Centre', 2),
(72, 'MALIETOA HINGANO', '1992-01-27', 'Centre', 2),
(73, 'PEYO MUSCARDITZ', '1996-01-02', 'Centre', 2),
(74, 'ROMAIN BARTHÉLÉMY', '1990-01-25', 'Centre', 2),
(75, 'ARTHUR DUHAU', '1997-08-09', 'Ailier', 2),
(76, 'DJIBRIL CAMARA', '1989-06-22', 'Ailier', 2),
(77, 'SEAN ROBINSON', '1993-11-02', 'Ailier', 2),
(78, 'AYMERIC LUC', '1997-10-14', 'Arrière', 2),
(79, 'JOHANNES PETRUS GRAAFF', '1989-09-10', 'Arrière', 2),
(80, 'JULIEN TISSERON', '1995-08-12', 'Arrière', 2),
(81, 'JEFFERSON POIROT', '1992-11-01', 'Pilier', 3),
(82, 'LASHA TABIDZE', '1997-07-04', 'Pilier', 3),
(83, 'LAURENT DELBOULBÈS', '1986-11-17', 'Pilier', 3),
(84, 'LEKSO KAULASHVILI', '1992-08-27', 'Pilier', 3),
(85, 'PENI RAVAI', '1990-06-16', 'Pilier', 3),
(86, 'THIERRY PAÏVA', '1995-11-19', 'Pilier', 3),
(87, 'VADIM COBILAS', '1983-07-30', 'Pilier', 3),
(88, 'ADRIEN PÉLISSIÉ', '1990-08-07', 'Talonneur', 3),
(89, 'CLÉMENT MAYNADIER', '1988-10-11', 'Talonneur', 3),
(90, 'ALEXANDRE FLANQUART', '1989-10-09', '2ème ligne', 3),
(91, 'CYRIL CAZEAUX', '1995-02-10', '2ème ligne', 3),
(92, 'JANDRÉ MARAIS', '1989-06-14', '2ème ligne', 3),
(93, 'KANE DOUGLAS', '1989-06-01', '2ème ligne', 3),
(94, 'MASALOSALO TUTAIA', '1984-06-05', '2ème ligne', 3),
(95, 'AFA AMOSA', '1990-10-11', '3ème ligne', 3),
(96, 'ALEXANDRE ROUMAT', '1997-06-27', '3ème ligne', 3),
(97, 'BÉKA GORGADZE', '1996-02-08', '3ème ligne', 3),
(98, 'CAMERON WOKI', '1998-11-07', '3ème ligne', 3),
(99, 'MAHAMADOU DIABY', '1990-08-15', '3ème ligne', 3),
(100, 'MARCO TAULEIGNE', '1993-08-30', '3ème ligne', 3),
(101, 'SCOTT HIGGINBOTHAM', '1986-09-05', '3ème ligne', 3),
(102, 'MAXIME LUCU', '1993-01-12', 'Mêlée', 3),
(103, 'YANN LESGOURGUES', '1991-01-17', 'Mêlée', 3),
(104, 'BEN BOTICA', '1989-10-07', 'Ouverture', 3),
(105, 'LUCAS MÉRET', '1995-01-30', 'Ouverture', 3),
(106, 'MATTHIEU JALIBERT', '1998-11-06', 'Ouverture', 3),
(107, 'JEAN-BAPTISTE DUBIÉ', '1989-07-16', 'Centre', 3),
(108, 'RÉMI LAMERAT', '1990-01-14', 'Centre', 3),
(109, 'SEMI RADRADRA', '1992-06-13', 'Centre', 3),
(110, 'SETA TAMANIVALU', '1992-07-23', 'Centre', 3),
(111, 'ULUPANO SEUTENI', '1993-12-09', 'Centre', 3),
(112, 'BLAIR CONNOR', '1988-09-29', 'Ailier', 3),
(113, 'NICOLAS PLAZY', '1994-05-17', 'Ailier', 3),
(114, 'SANTIAGO CORDERO', '1993-12-06', 'Ailier', 3),
(115, 'GEOFFREY CROS', '1997-03-08', 'Arrière', 3),
(116, 'NANS DUCUING', '1991-11-06', 'Arrière', 3),
(117, 'ROMAIN BUROS', '1997-07-31', 'Arrière', 3),
(118, 'CODY THOMAS', '1996-03-01', 'Pilier', 4),
(119, 'HAYDEN THOMPSON-STRINGER', '1994-12-25', 'Pilier', 4),
(120, 'JAMES JOHNSTON', '1986-03-06', 'Pilier', 4),
(121, 'KARLEN ASIESHVILI', '1987-04-21', 'Pilier', 4),
(122, 'MESAKE DOGE', '1993-04-01', 'Pilier', 4),
(123, 'SIMON-PIERRE CHAUVAC', '1998-03-23', 'Pilier', 4),
(124, 'SOSO BEKOSHVILI', '1993-11-03', 'Pilier', 4),
(125, 'FRANÇOIS DA ROS', '1983-09-29', 'Talonneur', 4),
(126, 'PENIAMI NASALI NARISIA', '1997-06-10', 'Talonneur', 4),
(127, 'THOMAS ACQUIER', '1989-11-21', 'Talonneur', 4),
(128, 'JAN UYS', '1994-01-03', '2ème ligne', 4),
(129, 'JOE SNYMAN', '1986-07-09', '2ème ligne', 4),
(130, 'MITCH LEES', '1988-10-12', '2ème ligne', 4),
(131, 'PEET MARAIS', '1990-10-31', '2ème ligne', 4),
(132, 'RICHARD FOURCADE', '1993-04-04', '2ème ligne', 4),
(133, 'VICTOR LEBAS', '1993-06-09', '2ème ligne', 4),
(134, 'ESTEBAN ABADIE', '1997-12-01', '3ème ligne', 4),
(135, 'IRAKLI TSKHADADZE', '1996-08-01', '3ème ligne', 4),
(136, 'KITIONE KAMIKAMICA', '1996-04-27', '3ème ligne', 4),
(137, 'MATTHIEU VOISIN', '1996-05-16', '3ème ligne', 4),
(138, 'OTAR GIORGADZE', '1996-03-02', '3ème ligne', 4),
(139, 'SAÏD HIRÈCHE', '1985-05-27', '3ème ligne', 4),
(140, 'SOOTALA FAASOO', '1994-10-02', '3ème ligne', 4),
(141, 'STEEVY CERQUEIRA', '1993-08-09', '3ème ligne', 4),
(142, 'DAVID DELARUE', '1996-10-27', 'Mêlée', 4),
(143, 'JULIEN BLANC', '1992-10-04', 'Mêlée', 4),
(144, 'QUENTIN DELORD', '1999-02-10', 'Mêlée', 4),
(145, 'VASIL LOBZHANIDZE', '1996-10-14', 'Mêlée', 4),
(146, 'ENZO HERVÉ', '1998-10-13', 'Ouverture', 4),
(147, 'THOMAS LARANJEIRA', '1992-05-05', 'Ouverture', 4),
(148, 'ALBAN RAMETTE', '1998-10-07', 'Centre', 4),
(149, 'ALEX DUNBAR', '1990-04-23', 'Centre', 4),
(150, 'ARNAUD MIGNARDI', '1986-11-01', 'Centre', 4),
(151, 'GUILLAUME GALLETIER', '1997-03-07', 'Centre', 4),
(152, 'NICO LEE', '1994-03-13', 'Centre', 4),
(153, 'SEVA GALALA', '1993-01-29', 'Centre', 4),
(154, 'STUART OLDING', '1993-03-11', 'Centre', 4),
(155, 'AXEL MULLER', '1993-11-25', 'Ailier', 4),
(156, 'FRANCK ROMANET', '1986-05-02', 'Ailier', 4),
(157, 'GUILLAUME NAMY', '1989-04-03', 'Ailier', 4),
(158, 'RORY SCHOLES', '1993-04-23', 'Ailier', 4),
(159, 'SETAREKI BITUNIYATA', '1995-08-12', 'Ailier', 4),
(160, 'JORIS JURAND', '1995-11-11', 'Arrière', 4),
(161, 'RICO BULIRUARUA', '1997-01-23', 'Arrière', 4),
(162, 'ANTOINE TICHIT', '1989-06-13', 'Pilier', 5),
(163, 'DANIEL KOTZE', '1987-03-28', 'Pilier', 5),
(164, 'KARENA WIHONGI', '1979-09-29', 'Pilier', 5),
(165, 'MARC CLERC', '1987-06-09', 'Pilier', 5),
(166, 'MATT TIERNEY', '1996-07-04', 'Pilier', 5),
(167, 'PAEA FAANUNU', '1988-11-04', 'Pilier', 5),
(168, 'TAPU FALATEA', '1988-12-12', 'Pilier', 5),
(169, 'TUDOR STROË', '1993-09-06', 'Pilier', 5),
(170, 'WAYAN DE BENEDITTIS', '1999-03-10', 'Pilier', 5),
(171, 'WILFRID HOUNKPATIN', '1991-07-29', 'Pilier', 5),
(172, 'JODY JENNEKER', '1984-04-10', 'Talonneur', 5),
(173, 'KÉVIN FIRMIN', '1992-04-20', 'Talonneur', 5),
(174, 'MARC-ANTOINE RALLIER', '1988-12-02', 'Talonneur', 5),
(175, 'PAUL SAUZARET', '1997-03-04', 'Talonneur', 5),
(176, 'CHRISTOPHE SAMSON', '1984-03-01', '2ème ligne', 5),
(177, 'HANS NKINSI', '1992-09-21', '2ème ligne', 5),
(178, 'LOÏC JACQUET', '1985-03-31', '2ème ligne', 5),
(179, 'RODRIGO CAPO ORTEGA', '1980-12-08', '2ème ligne', 5),
(180, 'VICTOR MOREAUX', '1993-09-19', '2ème ligne', 5),
(181, 'ALEX TULOU', '1987-03-21', '3ème ligne', 5),
(182, 'ANTHONY JELONCH', '1996-07-28', '3ème ligne', 5),
(183, 'BAPTISTE DELAPORTE', '1997-03-27', '3ème ligne', 5),
(184, 'CAMILLE GÉRONDEAU', '1988-03-12', '3ème ligne', 5),
(185, 'DORIAN CLERC', '1998-07-07', '3ème ligne', 5),
(186, 'KÉVIN GIMENO', '1991-09-11', '3ème ligne', 5),
(187, 'MAAMA VAIPULU', '1989-07-21', '3ème ligne', 5),
(188, 'MATHIEU BABILLOT', '1993-09-09', '3ème ligne', 5),
(189, 'LUDOVIC RADOSAVLJEVIC', '1989-08-17', 'Mêlée', 5),
(190, 'RORY KOCKOTT', '1986-06-25', 'Mêlée', 5),
(191, 'BENJAMIN URDAPILLETA', '1986-03-11', 'Ouverture', 5),
(192, 'THOMAS FORTUNEL', '1995-06-07', 'Ouverture', 5),
(193, 'FLORIAN VIALELLE', '1993-10-05', 'Centre', 5),
(194, 'ROBERT EBERSOHN', '1989-02-23', 'Centre', 5),
(195, 'THOMAS COMBEZOU', '1987-01-26', 'Centre', 5),
(196, 'YANN DAVID', '1988-04-15', 'Centre', 5),
(197, 'ARMAND BATLLE', '1987-04-12', 'Ailier', 5),
(198, 'BENJAMIN LAPEYRE', '1986-09-24', 'Ailier', 5),
(199, 'FILIPO NAKOSI', '1992-04-08', 'Ailier', 5),
(200, 'JULIEN CAMINATI', '1985-10-28', 'Ailier', 5),
(201, 'MARTIN LAVEAU', '1996-09-10', 'Ailier', 5),
(202, 'TAYLOR PARIS', '1992-10-06', 'Ailier', 5),
(203, 'GEOFFREY PALIS', '1991-07-08', 'Arrière', 5),
(204, 'JULIEN DUMORA', '1988-03-24', 'Arrière', 5),
(248, 'ARTHUR JOLY', '1988-02-20', 'Pilier', 7),
(249, 'DANY PRISO', '1994-01-02', 'Pilier', 7),
(250, 'MIKE CORBEL', '1992-04-09', 'Pilier', 7),
(251, 'RAMIRO HERRERA', '1989-02-14', 'Pilier', 7),
(252, 'REDA WARDI', '1995-08-02', 'Pilier', 7),
(253, 'SILA PUAFISI', '1988-04-15', 'Pilier', 7),
(254, 'UINI ATONIO', '1990-03-26', 'Pilier', 7),
(255, 'VINCENT PELO', '1988-04-22', 'Pilier', 7),
(256, 'FACUNDO BOSCH', '1991-08-08', 'Talonneur', 7),
(257, 'JEAN-CHARLES ORIOLI', '1989-08-09', 'Talonneur', 7),
(258, 'PIERRE BOURGARIT', '1997-09-12', 'Talonneur', 7),
(259, 'JONE QOVU', '1985-07-26', '2ème ligne', 7),
(260, 'MATHIEU TANGUY', '1996-06-05', '2ème ligne', 7),
(261, 'ROMAIN SAZY', '1986-10-14', '2ème ligne', 7),
(262, 'THOMAS JOLMÈS', '1995-10-08', '2ème ligne', 7),
(263, 'THOMAS LAVAULT', '1999-05-03', '2ème ligne', 7),
(264, 'KÉVIN GOURDON', '1990-01-23', '3ème ligne', 7),
(265, 'LOPETI TIMANI', '1990-09-28', '3ème ligne', 7),
(266, 'RÉMI BOURDEAU', '1992-02-27', '3ème ligne', 7),
(267, 'VICTOR VITO', '1987-03-27', '3ème ligne', 7),
(268, 'WIAAN LIEBENBERG', '1992-08-31', '3ème ligne', 7),
(269, 'ZENO KIEFT', '1991-11-02', '3ème ligne', 7),
(270, 'ALEXI BALÈS', '1990-05-30', 'Mêlée', 7),
(271, 'TAWERA KERR-BARLOW', '1990-08-15', 'Mêlée', 7),
(272, 'BROCK JAMES', '1981-10-22', 'Ouverture', 7),
(273, 'IHAIA WEST', '1992-01-16', 'Ouverture', 7),
(274, 'MAXIME LAFAGE', '1994-09-01', 'Ouverture', 7),
(275, 'BRIEUC PLESSIS-COUILLAUD', '1994-03-19', 'Centre', 7),
(276, 'GEOFFREY DOUMAYROU', '1989-09-16', 'Centre', 7),
(277, 'JÉRÉMY SINZELLE', '1990-07-02', 'Centre', 7),
(278, 'JULES FAVRE', '1999-03-22', 'Centre', 7),
(279, 'LEVANI BOTIA', '1989-03-14', 'Centre', 7),
(280, 'PIERRE AGUILLON', '1987-03-27', 'Centre', 7),
(281, 'ARTHUR RETIÈRE', '1997-08-01', 'Ailier', 7),
(282, 'ELIOTT ROUDIL', '1996-10-30', 'Ailier', 7),
(283, 'GABRIEL LACROIX', '1993-10-19', 'Ailier', 7),
(284, 'MARC ANDREU', '1985-12-27', 'Ailier', 7),
(285, 'KINI MURIMURIVALU', '1989-05-15', 'Arrière', 7),
(286, 'VINCENT RATTEZ', '1992-03-24', 'Arrière', 7),
(287, 'CLÉMENT RIC', '1988-07-18', 'Pilier', 8),
(288, 'FRANCISCO GOMEZ KODELA', '1985-07-03', 'Pilier', 8),
(289, 'HAMZA KAABÈCHE', '1996-09-23', 'Pilier', 8),
(290, 'RAPHAËL CHAUME', '1989-04-29', 'Pilier', 8),
(291, 'VIVIEN DEVISME', '1992-03-23', 'Pilier', 8),
(292, 'XAVIER CHIOCCI', '1990-02-13', 'Pilier', 8),
(293, 'BADRI ALKHAZASHVILI', '1995-07-31', 'Talonneur', 8),
(294, 'JÉRÉMIE MAUROUARD', '1992-09-23', 'Talonneur', 8),
(295, 'MICKAËL IVALDI', '1990-02-20', 'Talonneur', 8),
(296, 'ETIENNE OOSTHUIZEN', '1992-12-22', '2ème ligne', 8),
(297, 'FÉLIX LAMBEY', '1994-03-15', '2ème ligne', 8),
(298, 'HENDRIK ROODT', '1987-11-06', '2ème ligne', 8),
(299, 'KILIAN GÉRACI', '1999-03-25', '2ème ligne', 8),
(300, 'VIRGILE BRUNI', '1989-02-06', '2ème ligne', 8),
(301, 'CARL FEARNS', '1989-05-28', '3ème ligne', 8),
(302, 'DYLAN CRETIN', '1997-05-04', '3ème ligne', 8),
(303, 'JULIEN PURICELLI', '1981-08-01', '3ème ligne', 8),
(304, 'LIAM GILL', '1992-06-08', '3ème ligne', 8),
(305, 'LOANN GOUJON', '1989-04-23', '3ème ligne', 8),
(306, 'PATRICK SOBELA', '1992-08-12', '3ème ligne', 8),
(307, 'TANGINOA HALAIFONUA', '1996-08-03', '3ème ligne', 8),
(308, 'BAPTISTE COUILLOUD', '1997-07-22', 'Mêlée', 8),
(309, 'JONATHAN PÉLISSIÉ', '1988-06-06', 'Mêlée', 8),
(310, 'JEAN-MARC DOUSSAIN', '1991-02-12', 'Ouverture', 8),
(311, 'JONATHAN WISNIEWSKI', '1985-07-16', 'Ouverture', 8),
(312, 'PATRICIO FERNANDEZ', '1994-10-11', 'Ouverture', 8),
(313, 'CHARLIE NGATAI', '1990-08-17', 'Centre', 8),
(314, 'MATHIEU BASTAREAUD', '1988-09-17', 'Centre', 8),
(315, 'PIERRE-LOUIS BARASSI', '1998-04-22', 'Centre', 8),
(316, 'RUDI WULF', '1984-02-02', 'Centre', 8),
(317, 'THIBAUT REGARD', '1993-08-06', 'Centre', 8),
(318, 'ALEXIS PALISSON', '1987-09-09', 'Ailier', 8),
(319, 'JOSUA TUISOVA', '1994-02-04', 'Ailier', 8),
(320, 'NOA NAKAITACI', '1990-07-11', 'Ailier', 8),
(321, 'TOBY ARNOLD', '1987-09-11', 'Ailier', 8),
(322, 'XAVIER MIGNOT', '1994-01-27', 'Ailier', 8),
(323, 'CLÉMENT LAPORTE', '1998-01-07', 'Arrière', 8),
(324, 'JEAN-MARCELLIN BUTTIN', '1991-12-16', 'Arrière', 8),
(325, 'ANTOINE GUILLAMON', '1991-06-04', 'Pilier', 9),
(326, 'DANIEL BRENNAN', '1998-09-23', 'Pilier', 9),
(327, 'GRÉGORY FICHTEN', '1990-08-13', 'Pilier', 9),
(328, 'JANNIE DU PLESSIS', '1982-11-16', 'Pilier', 9),
(329, 'LEVAN CHILACHAVA', '1991-08-17', 'Pilier', 9),
(330, 'LIZO GQOBOKA', '1990-03-24', 'Pilier', 9),
(331, 'LUKA AZARIASHVILI', '1999-11-30', 'Pilier', 9),
(332, 'MISHA NARIASHVILI', '1990-05-25', 'Pilier', 9),
(333, 'MOHAMED HAOUAS', '1994-03-09', 'Pilier', 9),
(334, 'BISMARCK DU PLESSIS', '1984-05-22', 'Talonneur', 9),
(335, 'GUILHEM GUIRADO', '1986-06-17', 'Talonneur', 9),
(336, 'RONAN CHAMBORD', '1994-04-11', 'Talonneur', 9),
(337, 'VALENTIN SEILLÉ', '1999-04-07', 'Talonneur', 9),
(338, 'VINCENT GIUDICELLI', '1997-06-25', 'Talonneur', 9),
(339, 'YOURI DELHOMMEL', '1996-03-06', 'Talonneur', 9),
(340, 'JACQUES DU PLESSIS', '1993-08-12', '2ème ligne', 9),
(341, 'JULIEN LEDEVEDEC', '1986-06-04', '2ème ligne', 9),
(342, 'KONSTANTINE MIKAUTADZE', '1991-07-01', '2ème ligne', 9),
(343, 'NICOLAAS JANSE VAN RENSBURG', '1994-05-06', '2ème ligne', 9),
(344, 'PAUL WILLEMSE', '1992-11-13', '2ème ligne', 9),
(345, 'CALEB TIMU', '1994-02-22', '3ème ligne', 9),
(346, 'FULGENCE OUEDRAOGO', '1986-07-21', '3ème ligne', 9),
(347, 'JULIEN BARDY', '1986-04-03', '3ème ligne', 9),
(348, 'KÉLIAN GALLETIER', '1992-03-18', '3ème ligne', 9),
(349, 'KÉVIN KORNATH', '1996-12-27', '3ème ligne', 9),
(350, 'LOUIS PICAMOLES', '1986-02-05', '3ème ligne', 9),
(351, 'LUCAS DE CONINCK', '1996-01-15', '3ème ligne', 9),
(352, 'MARTIN DEVERGIE', '1995-06-26', '3ème ligne', 9),
(353, 'YACOUBA CAMARA', '1994-06-02', '3ème ligne', 9),
(354, 'BENOÎT PAILLAUGUE', '1987-11-17', 'Mêlée', 9),
(355, 'ENZO SANGA', '1995-05-19', 'Mêlée', 9),
(356, 'KAHN FOTUALII', '1982-05-22', 'Mêlée', 9),
(357, 'AARON CRUDEN', '1989-01-08', 'Ouverture', 9),
(358, 'HANDRÉ POLLARD', '1994-03-11', 'Ouverture', 9),
(359, 'THOMAS DARMON', '1998-05-12', 'Ouverture', 9),
(360, 'ARTHUR VINCENT', '1999-09-30', 'Centre', 9),
(361, 'FRANÇOIS STEYN', '1987-05-14', 'Centre', 9),
(362, 'JAN SERFONTEIN', '1993-04-15', 'Centre', 9),
(363, 'VINCENT MARTIN', '1992-09-04', 'Centre', 9),
(364, 'YVAN REILHAC', '1995-06-09', 'Centre', 9),
(365, 'GABRIEL NGANDEBE', '1997-03-30', 'Ailier', 9),
(366, 'NEMANI NADOLO', '1988-01-31', 'Ailier', 9),
(367, 'PIERRE TOURNEBIZE', '1998-09-25', 'Ailier', 9),
(368, 'TIMOCI NAGUSA', '1987-07-14', 'Ailier', 9),
(369, 'ANTHONY BOUTHIER', '1992-06-19', 'Arrière', 9),
(370, 'BENJAMIN FALL', '1989-03-03', 'Arrière', 9),
(371, 'HENRY IMMELMAN', '1995-05-26', 'Arrière', 9),
(372, 'JOHAN GOOSEN', '1992-07-27', 'Arrière', 9),
(373, 'CARLÜ SADIE', '1997-03-07', 'Pilier', 10),
(374, 'CHRISTOPHER VAOTOA', '1996-11-16', 'Pilier', 10),
(375, 'GIORGI MELIKIDZE', '1996-05-24', 'Pilier', 10),
(376, 'LUKE TAGI', '1997-06-23', 'Pilier', 10),
(377, 'PAUL ALO-EMILE', '1991-12-22', 'Pilier', 10),
(378, 'QUENTIN BÉTHUNE', '1995-09-25', 'Pilier', 10),
(379, 'SAMI MAVINGA', '1993-05-25', 'Pilier', 10),
(380, 'STÉPHANE CLÉMENT', '1987-09-03', 'Pilier', 10),
(381, 'THIERRY FUTEU', '1995-06-23', 'Pilier', 10),
(382, 'DAMIEN FITZPATRICK', '1989-06-08', 'Talonneur', 10),
(383, 'LAURENT PANIS', '1993-04-23', 'Talonneur', 10),
(384, 'LUCAS DA SILVA', '1997-12-19', 'Talonneur', 10),
(385, 'RÉMI BONFILS', '1988-09-26', 'Talonneur', 10),
(386, 'SIONE ANGAAELANGI', '1988-11-07', 'Talonneur', 10),
(387, 'TOLU LATU', '1993-02-23', 'Talonneur', 10),
(388, 'HUGH PYLE', '1988-09-21', '2ème ligne', 10),
(389, 'MATHIEU DE GIOVANNI', '1994-01-10', '2ème ligne', 10),
(390, 'PAUL GABRILLAGUES', '1993-06-03', '2ème ligne', 10),
(391, 'PIERRE-HENRI AZAGOH', '1998-07-25', '2ème ligne', 10),
(392, 'YOANN MAESTRI', '1988-01-14', '2ème ligne', 10),
(393, 'ANTOINE BURBAN', '1987-07-22', '3ème ligne', 10),
(394, 'CHARLIE FRANCOZ', '1998-06-03', '3ème ligne', 10),
(395, 'JOKETANI KOROI', '1996-01-01', '3ème ligne', 10),
(396, 'JOSH STRAUSS', '1986-10-23', '3ème ligne', 10),
(397, 'LOÏC GODENER', '1995-08-13', '3ème ligne', 10),
(398, 'PABLO MATERA', '1993-07-18', '3ème ligne', 10),
(399, 'RYAN CHAPUIS', '1997-12-12', '3ème ligne', 10),
(400, 'SEKOU MACALOU', '1995-04-20', '3ème ligne', 10),
(401, 'TALALELEI GRAY', '1990-02-28', '3ème ligne', 10),
(402, 'WILLEM ALBERTS', '1984-05-11', '3ème ligne', 10),
(403, 'ARTHUR COVILLE', '1998-02-04', 'Mêlée', 10),
(404, 'CLÉMENT DAGUIN', '1992-05-25', 'Mêlée', 10),
(405, 'JAMES HALL', '1996-01-02', 'Mêlée', 10),
(406, 'JORIS SEGONDS', '1997-04-06', 'Ouverture', 10),
(407, 'JULES PLISSON', '1991-08-20', 'Ouverture', 10),
(408, 'MORNÉ STEYN', '1984-07-11', 'Ouverture', 10),
(409, 'NICOLAS SANCHEZ', '1988-10-26', 'Ouverture', 10),
(410, 'ALEX ARRATE', '1997-06-24', 'Centre', 10),
(411, 'GAËL FICKOU', '1994-03-26', 'Centre', 10),
(412, 'JONATHAN DANTY', '1992-10-07', 'Centre', 10),
(413, 'JULIEN DELBOUIS', '1999-08-04', 'Centre', 10),
(414, 'LIONEL MAPOE', '1988-07-13', 'Centre', 10),
(415, 'ADRIEN LAPÈGUE', '1998-10-21', 'Ailier', 10),
(416, 'JULIEN ARIAS', '1983-10-26', 'Ailier', 10),
(417, 'LESTER ETIEN', '1995-06-21', 'Ailier', 10),
(418, 'RUAN COMBRINCK', '1990-05-10', 'Ailier', 10),
(419, 'SEFA NAIVALU', '1992-01-07', 'Ailier', 10),
(420, 'WAISEA NAYACALEVU', '1990-06-26', 'Ailier', 10),
(421, 'KYLAN HAMDAOUI', '1994-04-15', 'Arrière', 10),
(422, 'GEOFFREY MOÏSE', '1991-08-20', 'Pilier', 11),
(423, 'IGNACIO CALLES', '1995-10-24', 'Pilier', 11),
(424, 'LOURENS ADRIAANSE', '1988-02-05', 'Pilier', 11),
(425, 'LUCAS POINTUD', '1988-01-18', 'Pilier', 11),
(426, 'MALIK HAMADACHE', '1988-10-17', 'Pilier', 11),
(427, 'MOHAMED BOUGHANMI', '1991-10-27', 'Pilier', 11),
(428, 'NICOLAS CORATO', '1997-10-07', 'Pilier', 11),
(429, 'SIEGFRIED FISIIHOI', '1987-08-06', 'Pilier', 11),
(430, 'LUCAS REY', '1997-04-27', 'Talonneur', 11),
(431, 'QUENTIN LESPIAUCQ-BRETTES', '1995-02-16', 'Talonneur', 11),
(432, 'DAN MALAFOSSE', '1992-01-14', '2ème ligne', 11),
(433, 'DANIEL RAMSAY', '1984-06-01', '2ème ligne', 11),
(434, 'DENIS MARCHOIS', '1994-02-05', '2ème ligne', 11),
(435, 'FABRICE METZ', '1991-01-23', '2ème ligne', 11),
(436, 'JULIEN DELANNOY', '1995-06-15', '2ème ligne', 11),
(437, 'ANTOINE ERBANI', '1990-02-07', '3ème ligne', 11),
(438, 'BAPTISTE PESENTI', '1997-07-03', '3ème ligne', 11),
(439, 'CLÉMENT FOURNIER', '2000-05-06', '3ème ligne', 11),
(440, 'DOMINIKO WAQANIBUROTU', '1986-04-20', '3ème ligne', 11),
(441, 'GIOVANNI HABEL-KUEFFNER', '1995-01-09', '3ème ligne', 11),
(442, 'LEKIMA TAGITAGIVALU', '1995-12-12', '3ème ligne', 11),
(443, 'LUKE WHITELOCK', '1991-01-29', '3ème ligne', 11),
(444, 'MARTIN PUECH', '1988-12-14', '3ème ligne', 11),
(445, 'MATTHIEU UGENA', '1995-07-25', '3ème ligne', 11),
(446, 'PIERRICK GUNTHER', '1989-10-16', '3ème ligne', 11),
(447, 'CLOVIS LE BAIL', '1995-11-29', 'Mêlée', 11),
(448, 'SAMUEL MARQUÈS', '1988-12-08', 'Mêlée', 11),
(449, 'THIBAULT DAUBAGNA', '1994-05-20', 'Mêlée', 11),
(450, 'ANTOINE HASTOY', '1997-06-04', 'Ouverture', 11),
(451, 'COLIN SLADE', '1987-10-10', 'Ouverture', 11),
(452, 'TOM TAYLOR', '1989-03-11', 'Ouverture', 11),
(453, 'ALEXANDRE DUMOULIN', '1989-08-24', 'Centre', 11),
(454, 'ATILA SEPTAR', '1996-06-02', 'Centre', 11),
(455, 'BENSON STANLEY', '1984-09-11', 'Centre', 11),
(456, 'FLORIAN NICOT', '1986-09-30', 'Centre', 11),
(457, 'JALE VATUBUA', '1991-08-30', 'Centre', 11),
(458, 'JULIEN FUMAT', '1987-03-26', 'Centre', 11),
(459, 'PIERRE NUENO', '1996-05-15', 'Centre', 11),
(460, 'BASTIEN POURAILLY', '1994-01-31', 'Ailier', 11),
(461, 'BEN SMITH', '1986-06-01', 'Ailier', 11),
(462, 'VINCENT PINTO', '1999-04-10', 'Ailier', 11),
(463, 'WATISONI VOTU', '1985-03-25', 'Ailier', 11),
(464, 'CHARLY MALIÉ', '1991-11-05', 'Arrière', 11),
(465, 'JESSE MOGG', '1989-06-08', 'Arrière', 11),
(466, 'ALI OZ', '1995-05-28', 'Pilier', 12),
(467, 'BEN TAMEIFUNA', '1991-08-30', 'Pilier', 12),
(468, 'CEDATE GOMES SA', '1993-08-07', 'Pilier', 12),
(469, 'EDDY BEN AROUS', '1990-08-25', 'Pilier', 12),
(470, 'GEORGES-HENRI COLOMBE', '1998-04-09', 'Pilier', 12),
(471, 'HASSANE KOLINGAR', '1998-03-06', 'Pilier', 12),
(472, 'VASIL KAKOVIN', '1989-12-01', 'Pilier', 12),
(473, 'CAMILLE CHAT', '1995-12-18', 'Talonneur', 12),
(474, 'ISSAM HAMEL', '1997-06-18', 'Talonneur', 12),
(475, 'KÉVIN LE GUEN', '1990-11-17', 'Talonneur', 12),
(476, 'TEDDY BAUBIGNY', '1998-09-02', 'Talonneur', 12),
(477, 'DOMINIC BIRD', '1991-04-09', '2ème ligne', 12),
(478, 'DONNACHA RYAN', '1983-12-11', '2ème ligne', 12),
(479, 'LEONE NAKARAWA', '1988-02-04', '2ème ligne', 12),
(480, 'ANTONIE CLAASSEN', '1984-10-20', '3ème ligne', 12),
(481, 'BAPTISTE CHOUZENOUX', '1993-08-07', '3ème ligne', 12),
(482, 'BERNARD LE ROUX', '1989-06-04', '3ème ligne', 12),
(483, 'BORIS PALU', '1996-02-04', '3ème ligne', 12),
(484, 'FABIEN SANCONNIE', '1995-02-21', '3ème ligne', 12),
(485, 'IBRAHIM DIALLO', '1998-01-23', '3ème ligne', 12),
(486, 'JORDAN JOSEPH', '2000-07-31', '3ème ligne', 12),
(487, 'WENCESLAS LAURET', '1989-03-28', '3ème ligne', 12),
(488, 'YOAN TANGA-MANGENE', '1996-11-29', '3ème ligne', 12),
(489, 'ANTOINE GIBERT', '1997-12-31', 'Mêlée', 12),
(490, 'MAXIME MACHENAUD', '1988-12-30', 'Mêlée', 12),
(491, 'SAM HIDALGO-CLYNE', '1993-08-04', 'Mêlée', 12),
(492, 'TEDDY IRIBAREN', '1990-09-25', 'Mêlée', 12),
(493, 'BEN VOLAVOLA', '1991-01-13', 'Ouverture', 12),
(494, 'FINN RUSSELL', '1992-09-23', 'Ouverture', 12),
(495, 'FRANÇOIS TRINH-DUC', '1986-11-11', 'Ouverture', 12),
(496, 'JOAQUIN DIAZ BONILLA', '1989-04-12', 'Ouverture', 12),
(497, 'HENRY CHAVANCY', '1988-05-22', 'Centre', 12),
(498, 'LÉONARD PARIS', '1996-03-20', 'Centre', 12),
(499, 'OLIVIER KLEMENCZAK', '1996-06-01', 'Centre', 12),
(500, 'VIRIMI VAKATAWA', '1992-05-01', 'Centre', 12),
(501, 'DORIAN LABORDE', '1996-12-30', 'Ailier', 12),
(502, 'JUAN IMHOFF', '1988-05-11', 'Ailier', 12),
(503, 'SIMON ZEBO', '1990-03-16', 'Ailier', 12),
(504, 'TEDDY THOMAS', '1993-09-18', 'Ailier', 12),
(505, 'BRICE DULIN', '1990-04-13', 'Arrière', 12),
(506, 'LOUIS DUPICHOT', '1995-09-23', 'Arrière', 12),
(507, 'BEKA GIGASHVILI', '1992-02-17', 'Pilier', 13),
(508, 'BRUCE DEVAUX', '1996-11-14', 'Pilier', 13),
(509, 'FLORIAN FRESIA', '1992-01-17', 'Pilier', 13),
(510, 'JEAN-BAPTISTE GROS', '1999-05-29', 'Pilier', 13),
(511, 'MARCEL VAN DER MERWE', '1990-10-24', 'Pilier', 13),
(512, 'SÉBASTIEN TAOFIFENUA', '1992-03-21', 'Pilier', 13),
(513, 'WILCO LOUW', '1994-07-20', 'Pilier', 13),
(514, 'ANTHONY ÉTRILLARD', '1993-03-21', 'Talonneur', 13),
(515, 'BASTIEN SOURY', '1995-03-18', 'Talonneur', 13),
(516, 'CHRISTOPHER TOLOFUA', '1993-12-31', 'Talonneur', 13),
(517, 'BRIAN ALAINUUESE', '1994-03-19', '2ème ligne', 13),
(518, 'CORENTIN VERNET', '1996-09-27', '2ème ligne', 13),
(519, 'EBEN ETZEBETH', '1991-10-29', '2ème ligne', 13),
(520, 'MAMUKA GORGODZE', '1984-07-14', '2ème ligne', 13),
(521, 'ROMAIN TAOFIFENUA', '1990-09-14', '2ème ligne', 13),
(522, 'SWAN REBBADJ', '1995-01-15', '2ème ligne', 13),
(523, 'CHARLES OLLIVON', '1993-05-11', '3ème ligne', 13),
(524, 'FACUNDO ISA', '1993-09-21', '3ème ligne', 13),
(525, 'LIAM MESSAM', '1984-03-25', '3ème ligne', 13),
(526, 'RAPHAËL LAKAFIA', '1988-10-28', '3ème ligne', 13),
(527, 'SERGIO PARISSE', '1983-09-12', '3ème ligne', 13),
(528, 'STÉPHANE ONAMBÉLÉ', '1993-02-12', '3ème ligne', 13),
(529, 'THOMAS HOARAU', '1995-06-01', '3ème ligne', 13),
(530, 'ANTHONY MÉRIC', '1995-02-15', 'Mêlée', 13),
(531, 'BAPTISTE SERIN', '1994-06-20', 'Mêlée', 13),
(532, 'LOUIS SCHREUDER', '1990-04-25', 'Mêlée', 13),
(533, 'RHYS WEBB', '1988-12-09', 'Mêlée', 13),
(534, 'ANTHONY BELLEAU', '1996-04-08', 'Ouverture', 13),
(535, 'LOUIS CARBONEL', '1999-02-04', 'Ouverture', 13),
(536, 'MATHIEU SMAÏLI', '1999-08-30', 'Ouverture', 13),
(537, 'BEN TEO', '1987-01-27', 'Centre', 13),
(538, 'DUNCAN PAIAAUA', '1995-01-20', 'Centre', 13),
(539, 'JULIAN SAVEA', '1990-08-07', 'Centre', 13),
(540, 'JULIEN HÉRITEAU', '1994-09-12', 'Centre', 13),
(541, 'THÉO DACHARY', '1997-03-26', 'Centre', 13),
(542, 'BRYCE HEEM ', '1989-01-18', 'Ailier', 13),
(543, 'DANIEL IKPEFAN', '1993-10-18', 'Ailier', 13),
(544, 'GABIN VILLIÈRE', '1995-12-13', 'Ailier', 13),
(545, 'MASIVESI DAKUWAQA', '1994-02-14', 'Ailier', 13),
(546, 'GERVAIS CORDIN', '1998-12-10', 'Arrière', 13),
(547, 'HUGO BONNEVAL', '1990-11-19', 'Arrière', 13),
(548, 'NEHE MILNER-SKUDDER', '1990-12-15', 'Arrière', 13),
(549, 'CHARLIE FAUMUINA', '1986-12-24', 'Pilier', 14),
(550, 'CLÉMENT CASTETS', '1996-05-05', 'Pilier', 14),
(551, 'CYRIL BAILLE', '1993-09-15', 'Pilier', 14),
(552, 'DORIAN ALDEGHERI', '1993-08-04', 'Pilier', 14),
(553, 'MAKS VAN DYK', '1992-01-21', 'Pilier', 14),
(554, 'PAULO TAFILI', '1996-02-15', 'Pilier', 14),
(555, 'RÉMY HUGUES', '1986-01-01', 'Pilier', 14),
(556, 'RODRIGUE NETI', '1995-04-26', 'Pilier', 14),
(557, 'GUILLAUME CRAMONT', '2000-12-29', 'Talonneur', 14),
(558, 'GUILLAUME MARCHAND', '1998-06-05', 'Talonneur', 14),
(559, 'JACO VISAGIE', '1992-07-08', 'Talonneur', 14),
(560, 'JULIEN MARCHAND', '1995-05-10', 'Talonneur', 14),
(561, 'TAKESHI HINO', '1990-01-20', 'Talonneur', 14),
(562, 'BASTIEN CHALUREAU', '1992-02-13', '2ème ligne', 14),
(563, 'FLORIAN VERHAEGHE', '1997-04-27', '2ème ligne', 14),
(564, 'IOSEFA TEKORI', '1983-12-17', '2ème ligne', 14),
(565, 'RICHIE ARNOLD', '1990-07-01', '2ème ligne', 14),
(566, 'RICHIE GRAY', '1989-08-24', '2ème ligne', 14),
(567, 'RORY ARNOLD', '1990-07-01', '2ème ligne', 14),
(568, 'ALBAN PLACINES', '1993-04-23', '3ème ligne', 14),
(569, 'ANTOINE MIQUEL', '1994-06-20', '3ème ligne', 14),
(570, 'CARL AXTENS', '1991-08-26', '3ème ligne', 14),
(571, 'FRANÇOIS CROS', '1994-03-25', '3ème ligne', 14),
(572, 'GILLIAN GALAN', '1991-08-07', '3ème ligne', 14),
(573, 'JEROME KAINO', '1983-04-06', '3ème ligne', 14),
(574, 'LOUIS-BENOÎT MADAULE', '1988-09-24', '3ème ligne', 14),
(575, 'RYNHARDT ELSTADT', '1989-12-20', '3ème ligne', 14),
(576, 'SELEVASIO TOLOFUA', '1997-05-31', '3ème ligne', 14),
(577, 'ANTOINE DUPONT', '1996-11-15', 'Mêlée', 14),
(578, 'PIERRE PAGÈS', '1990-05-16', 'Mêlée', 14),
(579, 'SÉBASTIEN BÉZY', '1991-11-22', 'Mêlée', 14),
(580, 'ROMAIN NTAMACK', '1999-05-01', 'Ouverture', 14),
(581, 'TRISTAN TEDDER', '1996-04-17', 'Ouverture', 14),
(582, 'ZACK HOLMES', '1990-05-30', 'Ouverture', 14),
(583, 'MAXIME MERMOZ', '1986-07-28', 'Centre', 14),
(584, 'PIERRE FOUYSSAC', '1995-03-17', 'Centre', 14),
(585, 'PITA AHKI', '1992-09-24', 'Centre', 14),
(586, 'THÉO BELAN', '1992-11-15', 'Centre', 14),
(587, 'ARTHUR BONNEVAL', '1995-05-31', 'Ailier', 14),
(588, 'CHESLIN KOLBE', '1993-10-28', 'Ailier', 14),
(589, 'LUCAS TAUZIN', '1998-05-21', 'Ailier', 14),
(590, 'SOFIANE GUITOUNE', '1989-03-27', 'Ailier', 14),
(591, 'WERNER KOK', '1993-01-27', 'Ailier', 14),
(592, 'YOANN HUGET', '1987-06-02', 'Ailier', 14),
(593, 'MATTHIS LEBEL', '1999-03-25', 'Arrière', 14),
(594, 'MAXIME MÉDARD', '1986-11-16', 'Arrière', 14),
(595, 'THOMAS RAMOS', '1995-07-23', 'Arrière', 14);

-- --------------------------------------------------------

--
-- Table structure for table `matchs`
--

DROP TABLE IF EXISTS `matchs`;
CREATE TABLE IF NOT EXISTS `matchs` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `ID_equipe_domicile` int DEFAULT NULL,
  `ID_equipe_exterieur` int DEFAULT NULL,
  `Date_matchs` date DEFAULT NULL,
  `Resultat_matchs` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `ID_equipe_domicile` (`ID_equipe_domicile`),
  KEY `ID_equipe_exterieur` (`ID_equipe_exterieur`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `matchs`
--

INSERT INTO `matchs` (`ID`, `ID_equipe_domicile`, `ID_equipe_exterieur`, `Date_matchs`, `Resultat_matchs`) VALUES
(1, 14, 7, '2023-09-01', '24-18'),
(2, 12, 6, '2023-09-01', '16-22'),
(3, 13, 9, '2023-09-08', '30-25'),
(4, 3, 5, '2023-09-08', '28-14'),
(5, 8, 11, '2023-09-15', '21-19'),
(6, 1, 7, '2023-09-15', '19-15'),
(7, 6, 13, '2023-09-22', '26-20'),
(8, 9, 3, '2023-09-22', '18-16'),
(9, 5, 8, '2023-09-29', '28-20'),
(10, 7, 1, '2023-09-29', '32-22'),
(11, 10, 4, '2023-10-06', '45-12'),
(12, 14, 11, '2023-10-06', '25-18'),
(13, 2, 12, '2023-10-13', '22-20'),
(14, 12, 1, '2023-10-13', '30-14'),
(15, 4, 7, '2023-10-20', '16-14'),
(16, 13, 10, '2023-10-20', '28-20'),
(17, 3, 2, '2023-10-27', '32-13'),
(18, 8, 9, '2023-10-27', '24-20'),
(19, 7, 6, '2023-11-03', '18-16'),
(20, 4, 11, '2023-11-03', '20-18'),
(21, 14, 12, '2023-11-10', '32-28'),
(22, 5, 10, '2023-11-10', '22-20'),
(23, 10, 2, '2023-11-17', '28-24'),
(24, 8, 6, '2023-11-17', '18-16'),
(25, 6, 9, '2023-11-24', '26-22'),
(26, 9, 1, '2023-11-24', '35-16'),
(27, 10, 5, '2023-12-01', '20-18'),
(28, 12, 11, '2023-12-01', '24-20'),
(29, 4, 14, '2023-12-08', '22-18'),
(30, 8, 3, '2023-12-08', '26-24'),
(31, 13, 9, '2023-12-15', '30-28'),
(32, 1, 12, '2023-12-15', '32-30'),
(33, 7, 2, '2023-12-22', '25-20'),
(34, 2, 5, '2023-12-22', '28-22'),
(35, 10, 11, '2023-12-29', '26-22'),
(36, 11, 3, '2023-12-29', '20-18');

-- --------------------------------------------------------

--
-- Table structure for table `participer`
--

DROP TABLE IF EXISTS `participer`;
CREATE TABLE IF NOT EXISTS `participer` (
  `ID_joueur` int DEFAULT NULL,
  `ID_matchs` int DEFAULT NULL,
  KEY `ID_joueur` (`ID_joueur`),
  KEY `ID_matchs` (`ID_matchs`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `participer`
--

INSERT INTO `participer` (`ID_joueur`, `ID_matchs`) VALUES
(1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `statistiques`
--

DROP TABLE IF EXISTS `statistiques`;
CREATE TABLE IF NOT EXISTS `statistiques` (
  `ID_joueur` int NOT NULL,
  `ID_matchs` int NOT NULL,
  `Duree_jeu` int DEFAULT NULL,
  `Nombre_essais` int DEFAULT NULL,
  `Nombre_penalites` int DEFAULT NULL,
  `Nombre_cartons` int DEFAULT NULL,
  PRIMARY KEY (`ID_joueur`,`ID_matchs`),
  KEY `ID_matchs` (`ID_matchs`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Dumping data for table `statistiques`
--

INSERT INTO `statistiques` (`ID_joueur`, `ID_matchs`, `Duree_jeu`, `Nombre_essais`, `Nombre_penalites`, `Nombre_cartons`) VALUES
(1, 1, 50, 5, 2, 0);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `joueur`
--
ALTER TABLE `joueur`
  ADD CONSTRAINT `joueur_ibfk_1` FOREIGN KEY (`ID_equipe`) REFERENCES `equipe` (`ID`);

--
-- Constraints for table `matchs`
--
ALTER TABLE `matchs`
  ADD CONSTRAINT `matchs_ibfk_1` FOREIGN KEY (`ID_equipe_domicile`) REFERENCES `equipe` (`ID`),
  ADD CONSTRAINT `matchs_ibfk_2` FOREIGN KEY (`ID_equipe_exterieur`) REFERENCES `equipe` (`ID`);

--
-- Constraints for table `participer`
--
ALTER TABLE `participer`
  ADD CONSTRAINT `participer_ibfk_1` FOREIGN KEY (`ID_joueur`) REFERENCES `joueur` (`ID`),
  ADD CONSTRAINT `participer_ibfk_2` FOREIGN KEY (`ID_matchs`) REFERENCES `matchs` (`ID`);

--
-- Constraints for table `statistiques`
--
ALTER TABLE `statistiques`
  ADD CONSTRAINT `statistiques_ibfk_1` FOREIGN KEY (`ID_joueur`) REFERENCES `joueur` (`ID`),
  ADD CONSTRAINT `statistiques_ibfk_2` FOREIGN KEY (`ID_matchs`) REFERENCES `matchs` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
