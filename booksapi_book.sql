-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: mariadb
-- Generation Time: Nov 02, 2022 at 05:53 AM
-- Server version: 10.8.3-MariaDB-1:10.8.3+maria~jammy
-- PHP Version: 8.0.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `books`
--

--
-- Dumping data for table `booksapi_book`
--

INSERT INTO `booksapi_book` (`id`, `title`, `author`, `price`) VALUES
(1, 'Northanger Abbey', 'Jane Austen', '18.20'),
(2, 'War and Peace', 'Leo Tolstoy', '12.70'),
(3, 'Huckleberry Finn', 'Mark Twain', '5.76'),
(4, 'Mrs. Dalloway', 'Virginia Wolf', '25.00'),
(19, 'Bleak House', 'Charles Dickens', '5.75');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
