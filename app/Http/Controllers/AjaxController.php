<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class AjaxController extends Controller
{

    public $output;
    public function submitAction()

    {

        // Define the command to run the Python script
            $command = escapeshellcmd('python C:\\Users\\moses\\Desktop\\opencv\\face.py');

            // Execute the command and capture the output
            $this->output = shell_exec($command);

            // Display the output

           if( $this->output == "moses"){

               return response()->json([
                   'redirect_url' => route('redirect.target')  // Use the name of the route you want to redirect to
               ]);
           }
        // Here, you can handle any logic you need (e.g., saving data, processing).
        
        // After processing, return a JSON response with the redirect URL.
    }

    public function redirectTarget()
    {
       $data =   ['p' => $this->output];
       
        return view('chat',['data' => $data]);  // Example: Show a new view after redirection
    }
}
