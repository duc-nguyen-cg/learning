const {Pool, Client} = require('pg');

const credentials = require('./connection.json');

async function poolDemo() {
    const pool = new Pool(credentials);
    const now = await pool.query('SELECt NOW()');
    await pool.end();

    return now;
}

async function clientDemo() {
    const client = new Client(credentials);
    await client.connect();
    const now = await client.query('SELECt NOW()');
    await client.end();

    return now;
}

// (async () => {
//     const poolResult = await poolDemo();
//     console.log("Time with pool: " + poolResult.rows[0]['now']);
  
//     const clientResult = await clientDemo();
//     console.log("Time with client: " + clientResult.rows[0]['now']);
//   })();



const pool = new Pool(credentials);

async function registerPerson(person) {
    const text = `
    INSERT INTO people (fullname, gender, phone, age)
    VALUES ($1, $2, $3, $4)
    RETURNING id`;
    const values = [person.fullname, person.gender, person.phone, person.age];
    return pool.query(text, values);
}


async function getPerson(personId) {
    const text = ` SELECT * FROM people WHERE id = $1`;
    const values = [personId];
    return pool.query(text, values);
}

async function removePerson(personId){
    const text = `DELETE FROM people WHERE id = $1`;
    const values = [personId];
    return pool.query(text, values);
}

async function updatePerson(person, personId) {
    const text = `UPDATE people set fullname = $1, gender = $2, phone = $3, age = $4 where id = $5`;
    const values = [person.fullname, person.gender, person.phone, person.age, personId];
    return pool.query(text, values);
}

(async() => {
    //create
    const registered = await registerPerson({
        fullname: "Alex",
        gender: "F",
        phone: "333333",
        age: "33"
    });
    const personId = registered.rows[0]["id"];
    console.log("Registered a person with id = " + personId);

    //find
    const getPersonResult = await getPerson(personId);
    console.log(JSON.stringify(getPersonResult.rows[0], null, "  "));

    //delete
    await removePerson(personId);

    //update
    await updatePerson({
        fullname: "Georgia",
        gender: "F",
        phone: "88888888",
        age: "25"
    }, 2);
    const getUpdatedPerson = await getPerson(2);
    console.log(JSON.stringify(getUpdatedPerson.rows[0], null, "  "))

    await pool.end();
})();

