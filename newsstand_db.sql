-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: crud_db:3306
-- Generation Time: Jan 19, 2022 at 04:39 PM
-- Server version: 8.0.27
-- PHP Version: 7.4.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `newsstand_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `editors`
--

CREATE TABLE `editors` (
  `ed_id` int NOT NULL,
  `ed_firstname` varchar(255) NOT NULL,
  `ed_lastname` varchar(255) NOT NULL,
  `ed_datestarted` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `editors`
--

INSERT INTO `editors` (`ed_id`, `ed_firstname`, `ed_lastname`, `ed_datestarted`) VALUES
(1, 'Katharine', 'Viner', 'June 2015'),
(2, 'John', 'Witherow', '2013'),
(3, 'Neil', 'McIntosh', 'February 2021'),
(4, 'Ryan', 'Smith', '2014'),
(5, 'Ken', 'Fisher', '1998'),
(6, 'Chris', 'Williams', '1994'),
(7, 'Larry', 'Dignan', '1991'),
(8, 'Dan', 'Thorp-Lancaster', '2016'),
(9, 'Brian', 'Krebs', 'December 2009');

-- --------------------------------------------------------

--
-- Table structure for table `sites`
--

CREATE TABLE `sites` (
  `news_id` int NOT NULL,
  `ed_id` int NOT NULL,
  `news_name` varchar(255) NOT NULL,
  `news_url` varchar(255) NOT NULL,
  `news_img_url` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `sites`
--

INSERT INTO `sites` (`news_id`, `ed_id`, `news_name`, `news_url`, `news_img_url`) VALUES
(1, 1, 'The Guardian', 'https://www.theguardian.com', '/static/images/the-guardian-logo.png'),
(2, 2, 'The Times', 'https://www.thetimes.co.uk/', '/static/images/The-Times-Logo.png'),
(3, 3, 'The Scotsman', 'https://www.scotsman.com/', '/static/images/scotsman.png'),
(4, 4, 'AnandTech', 'https://www.anandtech.com/', '/static/images/anand.png'),
(5, 5, 'Ars Technica', 'https://arstechnica.com/', '/static/images/Ars_Technica_logo.png'),
(6, 6, 'The Register', 'https://www.theregister.com/', '/static/images/Reg-logo-RED-copy.png'),
(7, 7, 'ZDNet', 'https://www.zdnet.com/', '/static/images/zdnet-logo-large.png'),
(8, 8, 'Windows Central', 'https://www.windowscentral.com/', '/static/images/new-wc-logo_0.png'),
(9, 9, 'Krebs On Security', 'https://krebsonsecurity.com/', '/static/images/kos-27-03-2021.png');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `editors`
--
ALTER TABLE `editors`
  ADD PRIMARY KEY (`ed_id`);

--
-- Indexes for table `sites`
--
ALTER TABLE `sites`
  ADD PRIMARY KEY (`news_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `editors`
--
ALTER TABLE `editors`
  MODIFY `ed_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `sites`
--
ALTER TABLE `sites`
  MODIFY `news_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
