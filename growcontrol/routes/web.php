<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\SensorController;
use App\Http\Controllers\ActorController;

Route::get('/', function () {
    return view('welcome');
});

Route::get('/sensors', [SensorController::class, 'index']);
Route::get('/actors', [ActorController::class, 'index']);
