Table users as U
{
  id int [pk, increment]
  type varchar
  power_used int
  time timestamp
}

Table generators as G
{
  id int [pk, increment]
  type varchar
  power_generated int
  time timestamp
}