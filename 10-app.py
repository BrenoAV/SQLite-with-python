import database

database.create_db()
database.show_all()
database.add_record("Monkey", "Luffy", "luffy@mugiwara.com")
database.show_all()
database.del_record("5")
database.show_all()
database.add_many_records(
    [
        ("Roronoa", "Zoro", "zoro@mugiwara.com"),
        ("Prince", "Vegeta", "vegeta@tournament.com"),
    ]
)
database.show_all()
database.email_lookup("%@vila.com")
