var gulp = require('gulp');

function defaultTask(callback) {
    console.log("it's a default task");
    callback();
}

gulp.task("greet", function(callback) {
    console.log("hello!");
    callback();
});

exports.default = defaultTask;