create database teachers_portal;
use teachers_portal;
create table students (
	studentId int not null unique auto_increment,
    studentName varchar(45) not null,
    enrolledInCourseID int default 1,
    grade float null,
    primary key (studentId)
);

create table courses (
	courseId int not null unique auto_increment,
    courseName varchar(45) not null,
    primary key (courseId)
);

insert into students (studentName, enrolledInCourseID, grade)
values ("Maria Jozef", 1, 90);

insert into students (studentName, enrolledInCourseID, grade)
values ("Linda Jones", 2, 89);

insert into students (studentName, enrolledInCourseID, grade)
values ("John McGrail", 1, 98);

insert into students (studentName, enrolledInCourseID, grade)
values ("Patty Luna", 2, 78);

insert into courses (courseName)
values ("Database Design");

insert into courses (courseName)
values ("Calculus");

insert into courses (courseName)
values ("Physics I");

delimiter $$
create procedure studentsWithGrade()
begin
	select * 
    from students
    left join courses on enrolledInCourseID = courseID;
end $$
delimiter ;

call studentsWithGrade();