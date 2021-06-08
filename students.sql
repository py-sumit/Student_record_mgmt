create database students;
use students;

--
-- Database: `students`
--

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `roll` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `dob` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `contact` int(10) NOT NULL,
  `marks` int(3) NOT NULL,
  `tmarks` int(3) NOT NULL,
  `address` varchar(200) NOT NULL,
  `attendence` varchar(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`roll`);
COMMIT;

create table teacher(
name VARCHAR(30),
cl VARCHAR(10),
username VARCHAR(12),
password VARCHAR(15),
primary key (username)
);

create table stu(
name VARCHAR(30),
cl VARCHAR(10),
username VARCHAR(12),
password VARCHAR(15),
primary key (username)
);
select * from students