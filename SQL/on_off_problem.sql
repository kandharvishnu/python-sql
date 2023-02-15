-- https://www.youtube.com/watch?v=XQ80MgsTka0
use sql_study;

create table event_status
(
event_time varchar(10),
status varchar(10)
);
insert into event_status 
values
('10:01','on'),('10:02','on'),('10:03','on'),('10:04','off'),('10:07','on'),('10:08','on'),('10:09','off')
,('10:11','on'),('10:12','off');

select * from event_status;

select min(event_time) login,max(lead_et) logout,count(*) cnt from
(select *, rnn-rn as diff from
(SELECT 
event_time,status, row_number() over (partition by status order by event_time) rn,
row_number() over(order by event_time) rnn,lead(event_time,1) over (order by event_time) as lead_et
from event_status)a)b where status='on'
group by diff
;
