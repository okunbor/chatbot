<?php
use App\Http\Controllers\AjaxController;

use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return view('welcome');
});


// Route::get("/chat",function ()  {
//     return view("chat");
// });



Route::post('/submit-action', [AjaxController::class, 'submitAction'])->name('ajax.post');

Route::get('/chat', [AjaxController::class, 'redirectTarget'])->name('redirect.target');
