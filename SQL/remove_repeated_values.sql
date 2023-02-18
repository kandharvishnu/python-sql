--https://www.youtube.com/watch?v=LJuGi0VRCA0&list=PLYUFWNUuw0fm89ZIcYHhNRTsB7RJzM1tX&index=1
use sql_study;

create table number_pairs(A int, B int);
insert into number_pairs values(1,2);
insert into number_pairs values(3,2);
insert into number_pairs values(2,4);
insert into number_pairs values(2,1);
insert into number_pairs values(5,6);
insert into number_pairs values(4,2);

select * from number_pairs;

select a.* from
number_pairs a LEFT join number_pairs b ON a.a=b.b and a.b=b.a
WHERE (a.a<b.a or b.a is null);
;