#onsen_inn_search


##Docker

Download Docker on your Mac or Windows <br />
Mac : https://hub.docker.com/editions/community/docker-ce-desktop-mac <br />
Windows : https://hub.docker.com/editions/community/docker-ce-desktop-windows (Windows)

Open Docker.


##Setup

```
$ docker-compose up
```


When you shut down jaran\_api

```
$ docker-compose down
```


##Development

When you want to work on the docker container

```
$ docker exec -it <container id of the onsen_inn_search_web> bash
```

or 

```
$ docker exec -it $(docker ps | grep onsen_inn_search_web | awk {'print $1'}) bash
```

When you run a command on the docker container

```
$ docker exec -i <container id of the onsen_inn_search_web> <command>
```

or

```
$ docker exec -i $(docker ps | grep onsen_inn_search_web | awk {'print $1'}) <command>
```


##Backup and restore database

Back up

```
$ docker exec <container id of the onsen_inn_search_web> pg_dump -U postgres postgres > db_data.sql
```

or 

```
$ docker exec $(docker ps | grep postgres | awk '{print $1}') pg_dump -U postgres postgres > db_data.sql
```

Restore

```
$ docker exec -i <container id of the onsen_inn_search_web> psql -U postgres -d postgres < db_data.sql
```

or 

```
$ docker exec -i $(docker ps | grep postgres | awk '{print $1}') psql -U postgres -d postgres < db_data.sql
```


##DB Schema

Onsen_Model<br />
    onsen_id Int(Not Null)<br />
    onsen_name Char(max_length=20, Not Null)<br />
    onsen_name_kana Char(max_length=30, Not Null)<br />
    onsen_address Char(max_length=30, Not Null)<br />
    region Char(max_length=10, Not Null)<br />
    prefecture Char(max_length=10, Not Null)<br />
    large_area Char(max_length=10, Not Null)<br />
    small_area Char(max_length=10, Not Null)<br />
    nature_of_onsen Char(max_length=10, Not Null)<br />
    onsen_area_name Char(max_length=20)<br />
    onsen_area_name_kana Char(max_length=30)<br />
    onsen_area_id Int()<br />
    onsen_area_caption Text()<br />

onsenInnModel<br />
    inn_id Int(Not Null)<br />
    inn_name Char(max_length=100, Not Null)<br />
    inn_photo Image()<br />
    inn_min_price Int(Not Null)<br />
    review_room Decimal(max_digits=2, decimal_places=1)<br />
    review_bath Decimal(max_digits=2, decimal_places=1)<br />
    review_breakfast Decimal(max_digits=2, decimal_places=1)<br />
    review_dinner Decimal(max_digits=2, decimal_places=1)<br />
    review_service Decimal(max_digits=2, decimal_places=1)<br />
    review_cleanes Decimal(max_digits=2, decimal_places=1)<br />
    rooms_total Int(Not Null)<br />
    baths_total Int(Not Null)<br />

    free_wifi Bool()<br />
    convenience_store Bool()<br />
    hand_towel Bool()<br />
    dental_amenities Bool()<br />
    bath_towel Bool()<br />
    shampoo Bool()<br />
    conditoner Bool()<br />
    body_wash Bool()<br />
    bar_soap Bool()<br />
    yukata Bool()<br />
    pajamas Bool()<br />
    bathrobe Bool()<br />
    dryer Bool()<br />
    duvet Bool()<br />
    razor Bool()<br />
    shower_cap Bool()<br />
    cotton_swab Bool()<br />
    onsui_toilet Bool()<br />
    hair_brush Bool()<br />
    onsen ForeignKey(onsenModel)<br />