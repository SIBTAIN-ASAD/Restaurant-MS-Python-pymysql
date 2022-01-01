-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 19, 2021 at 05:08 PM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 7.3.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rms`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `admin_id` int(10) NOT NULL,
  `admin_name` varchar(20) NOT NULL,
  `admin_pwd` varchar(20) NOT NULL,
  `admin_email` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`admin_id`, `admin_name`, `admin_pwd`, `admin_email`) VALUES
(1, 'RMS ADMIN', 'admin', 'admin@gmail.com'),
(2, 'Admin2', 'admin2', 'admin2@yahoo.com'),
(3, 'admin3', 'admin3', 'admin3@'),
(4, 'test', 'test', 'test'),
(5, 'Sibtain', 'sam123', 'sam@innovaxel.com');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `cus_id` int(10) NOT NULL,
  `cus_name` varchar(30) NOT NULL,
  `cus_pwd` varchar(30) NOT NULL,
  `cus_email` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`cus_id`, `cus_name`, `cus_pwd`, `cus_email`) VALUES
(1, 'cus1', '1234', 'cus@'),
(2, 'cus2', '1234', 'cus2@'),
(3, 'SAM', 'sam12345', 'sam@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `data`
--

CREATE TABLE `data` (
  `id` int(10) NOT NULL,
  `cus_email` varchar(30) NOT NULL,
  `dish` varchar(30) NOT NULL,
  `price` varchar(30) NOT NULL,
  `quantity` varchar(30) NOT NULL,
  `data_id` int(10) NOT NULL DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `data`
--

INSERT INTO `data` (`id`, `cus_email`, `dish`, `price`, `quantity`, `data_id`) VALUES
(2, 'cus@', 'Satay', '30', '1', 1),
(3, 'cus@', 'nougat', '40', '2', 1),
(4, 'cus@', 'Fish', '100', '3', 1),
(5, 'cus@', 'nougat', '40', '2', 1),
(6, 'cus@', 'nougat', '40', '2', 2),
(7, 'cus@', 'Pizza', '30', '3', 2),
(8, 'cus@', 'nougat', '40', '4', 3),
(9, 'cus@', 'Pizza', '30', '2', 3),
(10, 'cus@', 'Fish', '100', '3', 4),
(11, 'cus@', 'Pizza', '30', '4', 4),
(12, 'cus@', 'nougat', '40', '2', 4),
(13, 'cus@', 'nougat', '40', '2', 5),
(14, 'sam@gmail.com', 'Pizza', '30', '2', 6),
(15, 'sam@gmail.com', 'nougat', '40', '2', 6),
(16, 'sam@gmail.com', 'Pizza', '30', '2', 6);

-- --------------------------------------------------------

--
-- Table structure for table `dish`
--

CREATE TABLE `dish` (
  `d_id` int(10) NOT NULL,
  `d_name` varchar(30) NOT NULL,
  `d_ingredients` varchar(30) NOT NULL,
  `d_price` varchar(30) NOT NULL,
  `d_category` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dish`
--

INSERT INTO `dish` (`d_id`, `d_name`, `d_ingredients`, `d_price`, `d_category`) VALUES
(1, 'Satay', '1', '30', 'Meat'),
(2, 'nougat', '2', '40', 'dessert'),
(3, 'Fish', '3', '100', 'seafood'),
(4, 'Pizza', '5', '30', 'FastFood');

-- --------------------------------------------------------

--
-- Table structure for table `ingredients`
--

CREATE TABLE `ingredients` (
  `i_id` int(10) NOT NULL,
  `first` varchar(30) NOT NULL,
  `second` varchar(30) NOT NULL,
  `third` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ingredients`
--

INSERT INTO `ingredients` (`i_id`, `first`, `second`, `third`) VALUES
(1, 'meat', 'tofu', 'seafood'),
(2, 'torrone', 'mandolato', 'gaz'),
(3, 'cod', 'haddock', 'hake'),
(4, 'Cheez', 'Butter', 'Mayonees'),
(5, 'Cheez', 'Butter', 'Honey');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `id` int(10) NOT NULL,
  `email` varchar(30) NOT NULL,
  `type` varchar(30) NOT NULL DEFAULT 'dine',
  `payment` varchar(30) NOT NULL DEFAULT 'Cash'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`id`, `email`, `type`, `payment`) VALUES
(1, 'cus@', 'dine', 'Cash'),
(2, 'cus@', 'dine', 'Cash'),
(3, 'cus@', 'dine', 'Cash'),
(4, 'cus@', 'parcel', 'Credit_Card'),
(5, 'cus@', 'parcel', 'Credit_Card'),
(6, 'sam@gmail.com', 'dine', 'Cash');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`cus_id`);

--
-- Indexes for table `data`
--
ALTER TABLE `data`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dish`
--
ALTER TABLE `dish`
  ADD PRIMARY KEY (`d_id`);

--
-- Indexes for table `ingredients`
--
ALTER TABLE `ingredients`
  ADD PRIMARY KEY (`i_id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `admin_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `cus_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `data`
--
ALTER TABLE `data`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `dish`
--
ALTER TABLE `dish`
  MODIFY `d_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `ingredients`
--
ALTER TABLE `ingredients`
  MODIFY `i_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
