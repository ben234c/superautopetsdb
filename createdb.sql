select schema_name from information_schema.schemata where schema_name = 'sap'
use sap;
if not exists (select * from sap where name = 'pets')
begin
print 'pets does not exist'
create table pets (name varchar(50), tier tinyint, attack smallint, health smallint, token varchar(5))
end
-- create table runs (user_id varchar(50), startdate date, turns int, wins int, lives int, t3life tinyint(1), version int, run_id varchar(12), primary key (run_id));
-- create table turns (run_id varchar(12), turn_id varchar(15), gold int, lives int, turn int, wins int, p1name varchar(30), p1lvl int, p1hp int, p1atk int, p1perk int, p1trumpets int, p1mana int, p2name varchar(30), p2lvl int, p2hp int, p2atk int, p2perk int, p2trumpets int, p2mana int, p3name varchar(30), p3lvl int, p3hp int, p3atk int, p3perk int, p3trumpets int, p3mana int, p4name varchar(30), p4lvl int, p4hp int, p4atk int, p4perk int, p4trumpets int, p4mana int, p5name varchar(30), p5hp int, p5lvl int, p5atk int, p5perk int, p5trumpets int, p5mana int, primary key (turn_id), foreign key (run_id) references runs(run_id));



-- add lvl to columns

-- runs
-- user id, date, pack, turns, wins, lives, life recovery?/run id(randomly generated 12 digit alphanumeric)/version 

-- turns
-- run id, starting gold, lives, turn, wins, pet 1 name, pet 1 hp, pet 1 atk, pet 1 perk, pet 1 trumpets, pet 1 mana, ..., p5 mana,/ turn_id (randomly generated 15 digit alphanumeric)
