-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Ноя 21 2021 г., 11:15
-- Версия сервера: 10.4.21-MariaDB
-- Версия PHP: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `hoteldb`
--

-- --------------------------------------------------------

--
-- Структура таблицы `chef`
--

CREATE TABLE `chef` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `gender` int(20) NOT NULL,
  `room` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `chef`
--

INSERT INTO `chef` (`id`, `name`, `gender`, `room`) VALUES
(1, 'chef1', 2, 3);

-- --------------------------------------------------------

--
-- Структура таблицы `cleaning`
--

CREATE TABLE `cleaning` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `location` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Структура таблицы `gender`
--

CREATE TABLE `gender` (
  `id` int(11) NOT NULL,
  `type` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `gender`
--

INSERT INTO `gender` (`id`, `type`) VALUES
(1, 'male'),
(2, 'female');

-- --------------------------------------------------------

--
-- Структура таблицы `guest`
--

CREATE TABLE `guest` (
  `id` int(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `sname` varchar(20) NOT NULL,
  `gender` int(20) NOT NULL,
  `phone` int(20) NOT NULL,
  `room` int(20) NOT NULL,
  `city` varchar(20) NOT NULL,
  `country` varchar(20) NOT NULL,
  `date1` date NOT NULL,
  `dare2` date NOT NULL,
  `email` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `guest`
--

INSERT INTO `guest` (`id`, `name`, `sname`, `gender`, `phone`, `room`, `city`, `country`, `date1`, `dare2`, `email`) VALUES
(1, 'name1', 'sname1', 1, 781, 2, 'city1', 'country1', '2021-11-03', '2021-11-15', 'email1'),
(2, 'name1', 'sname1', 2, 1234, 3, 'city1', 'country1', '2021-11-11', '2021-11-12', 'email1');

-- --------------------------------------------------------

--
-- Структура таблицы `manager`
--

CREATE TABLE `manager` (
  `id` int(11) NOT NULL,
  `name` varchar(11) NOT NULL,
  `phone` int(11) NOT NULL,
  `gender` int(11) NOT NULL,
  `room` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `manager`
--

INSERT INTO `manager` (`id`, `name`, `phone`, `gender`, `room`) VALUES
(2, 'john', 1, 1, 3),
(3, 'Tom', 85, 1, 1),
(4, 'Ivan', 452, 1, 1),
(5, 'artem', 1234, 1, 3);

-- --------------------------------------------------------

--
-- Структура таблицы `receptionist`
--

CREATE TABLE `receptionist` (
  `id` int(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `gender` int(20) NOT NULL,
  `phone` int(20) NOT NULL,
  `room` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `receptionist`
--

INSERT INTO `receptionist` (`id`, `name`, `gender`, `phone`, `room`) VALUES
(1, 'name1', 1, 123, 4);

-- --------------------------------------------------------

--
-- Структура таблицы `room`
--

CREATE TABLE `room` (
  `id` int(10) NOT NULL,
  `location` varchar(20) NOT NULL,
  `type` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Дамп данных таблицы `room`
--

INSERT INTO `room` (`id`, `location`, `type`, `name`) VALUES
(1, 'location1', 'twin', 'room1'),
(2, 'location2', 'king', 'room2'),
(3, 'location3', 'kitchen', 'room3'),
(4, 'location4', 'king', 'name4');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `chef`
--
ALTER TABLE `chef`
  ADD PRIMARY KEY (`id`),
  ADD KEY `gender` (`gender`),
  ADD KEY `room` (`room`);

--
-- Индексы таблицы `cleaning`
--
ALTER TABLE `cleaning`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `gender`
--
ALTER TABLE `gender`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `guest`
--
ALTER TABLE `guest`
  ADD PRIMARY KEY (`id`),
  ADD KEY `room` (`room`),
  ADD KEY `gender` (`gender`);

--
-- Индексы таблицы `manager`
--
ALTER TABLE `manager`
  ADD PRIMARY KEY (`id`),
  ADD KEY `room` (`room`),
  ADD KEY `gender` (`gender`);

--
-- Индексы таблицы `receptionist`
--
ALTER TABLE `receptionist`
  ADD PRIMARY KEY (`id`),
  ADD KEY `room` (`room`),
  ADD KEY `gender` (`gender`);

--
-- Индексы таблицы `room`
--
ALTER TABLE `room`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `chef`
--
ALTER TABLE `chef`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT для таблицы `cleaning`
--
ALTER TABLE `cleaning`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `gender`
--
ALTER TABLE `gender`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `guest`
--
ALTER TABLE `guest`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `manager`
--
ALTER TABLE `manager`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `receptionist`
--
ALTER TABLE `receptionist`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT для таблицы `room`
--
ALTER TABLE `room`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `chef`
--
ALTER TABLE `chef`
  ADD CONSTRAINT `chef_ibfk_1` FOREIGN KEY (`gender`) REFERENCES `gender` (`id`),
  ADD CONSTRAINT `chef_ibfk_2` FOREIGN KEY (`room`) REFERENCES `room` (`id`);

--
-- Ограничения внешнего ключа таблицы `guest`
--
ALTER TABLE `guest`
  ADD CONSTRAINT `guest_ibfk_1` FOREIGN KEY (`room`) REFERENCES `room` (`id`),
  ADD CONSTRAINT `guest_ibfk_2` FOREIGN KEY (`gender`) REFERENCES `gender` (`id`);

--
-- Ограничения внешнего ключа таблицы `manager`
--
ALTER TABLE `manager`
  ADD CONSTRAINT `manager_ibfk_1` FOREIGN KEY (`room`) REFERENCES `room` (`id`),
  ADD CONSTRAINT `manager_ibfk_2` FOREIGN KEY (`gender`) REFERENCES `gender` (`id`);

--
-- Ограничения внешнего ключа таблицы `receptionist`
--
ALTER TABLE `receptionist`
  ADD CONSTRAINT `receptionist_ibfk_1` FOREIGN KEY (`room`) REFERENCES `room` (`id`),
  ADD CONSTRAINT `receptionist_ibfk_2` FOREIGN KEY (`gender`) REFERENCES `gender` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
