
table_name =  "APPLICANT"
schema = "TRADEMARK"
ids = "123"
entity_guid_update_stmt = ' '.join([
                "update TRADEMARK.{}.{} d set d.entity_guid = s.prev_guid from (".format(schema, table_name),
                "select a.id, a.inserted, {0}_name as name, {0}_address_country_code as country, entity_guid, ",
                "lead(entity_guid,1, entity_guid) over (PARTITION BY (a.id, a.ordinal) order by a.inserted desc) as prev_guid,",
                "lead({0}_name,1, {0}_name) over (PARTITION BY (a.id, a.ordinal) order by a.inserted desc) as prev_name,".format(table_name.lower()),
                "lead({0}_address_country_code,1, {0}_address_country_code) over (PARTITION BY (a.id, a.ordinal) order by a.inserted desc) as prev_country,".format(table_name.lower()),
                "row_number() over (PARTITION BY (a.id, a.ordinal) order by a.inserted desc) as row_num from TRADEMARK.{}.{} a ".format(schema, table_name),
                "join TRADEMARK.{}.TRADEMARK t on t.id = a.id and t.inserted=a.inserted and t.deleted = false and t.latest ".format(schema),
                "where id in ({})".format(str(ids)[1:-1]) if ids is not None else "",
                ")s where  row_num =1 and s.name = s.prev_name and s.country = s.prev_country and s.prev_guid is not null and s.entity_guid is null and s.id = d.id and s.inserted = d.inserted"
            ])
print("sql: ",entity_guid_update_stmt)