#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const tasks = JSON.parse(body);
  const userTasks = {};

  tasks.forEach(task => {
    if (task.completed) {
      if (userTasks[task.userId]) {
        userTasks[task.userId]++;
      } else {
        userTasks[task.userId] = 1;
      }
    }
  });

  console.log(userTasks);
});
