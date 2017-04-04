// started with: http://markgoodyear.com/2014/01/getting-started-with-gulp/

// get all the plugins
var gulp = require('gulp'),
    sass = require('gulp-sass'),
    postcss = require('gulp-postcss');
    autoprefixer = require('autoprefixer'),
    minifycss = require('gulp-clean-css'),
    jshint = require('gulp-jshint'),
    uglify = require('gulp-uglify'),
    rename = require('gulp-rename'),
    concat = require('gulp-concat'),
    notify = require('gulp-notify'),
    cache = require('gulp-cache'),
    livereload = require('gulp-livereload'),
    del = require('del'),
    scsslint = require('gulp-sass-lint'),
    imagemin = require('gulp-imagemin'),
    pngquant = require('imagemin-pngquant');

// Stop Gulp from crashing on every SASS error
// via: http://stackoverflow.com/questions/23971388/prevent-errors-from-breaking-crashing-gulp-watch/23973536#23973536
function swallowError (error) {
    //If you want details of the error in the console
    console.log(error.toString());

    this.emit('end');
}

// do CSS stuff
gulp.task('styles', function() {
  return gulp.src('sass/website/website.scss')
    .pipe(scsslint({config: 'scsslint.yml'}))
    .pipe(sass({ style: 'expanded' }))
    .on('error', swallowError)
    .pipe(postcss([ autoprefixer() ]))
    .pipe(gulp.dest('css'))
    .pipe(rename({suffix: '.min'}))
    .pipe(minifycss())
    .pipe(gulp.dest('css'))
    .pipe(notify({ message: 'Styles task complete' }));
});

// do JS stuff
// source scripts go in 'scripts' folder and are compiled into 'js'
// we're ignoring modernizr because we need that to be a separate file so we can load it in the head
gulp.task('scripts', function() {
  return gulp.src(['scripts/**/*.js', '!scripts/modernizr.js'])
    .pipe(jshint('.jshintrc'))
    .pipe(jshint.reporter('default'))
    .pipe(concat('app.js'))
    .pipe(gulp.dest('js'))
    .pipe(rename({suffix: '.min'}))
    .pipe(uglify())
    .pipe(gulp.dest('js'))
    .pipe(notify({ message: 'Scripts task complete' }));
});

// copy modernizr to the js directory
// this keeps the workflow consistent
gulp.task('scripts_copy', function(){
  return gulp.src('scripts/modernizr.js')
    .pipe(gulp.dest('js'));
});

// clean up
gulp.task('clean', function(cb) {
    del(['css', 'js'], cb)
});


// reduce image size
// More customizations at https://github.com/sindresorhus/gulp-imagemin
gulp.task('images', function() {
  return gulp.src('images/*')
    .pipe(imagemin({
        progressive: true,
        svgoPlugins: [
            {removeViewBox: false},
            {cleanupIDs: false}
        ],
        use: [pngquant()]
    }))
    .pipe(gulp.dest('img/'));
});


// watch task
gulp.task('watch', function() {

  // Watch .scss files
  gulp.watch('sass/**/*.scss', ['styles']);

  // Watch .js files
  gulp.watch('scripts/**/*.js', ['scripts', 'scripts_copy']);

  // Create LiveReload server
  livereload.listen();

  // Watch any files in dist/, reload on change
  gulp.watch(['css/**','js/**', '../**/*.php', '../**/*.html']).on('change', livereload.changed);

});

// default task
gulp.task('default', ['watch']);
