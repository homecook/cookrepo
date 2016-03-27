package homecook.comocasa;

import android.content.Intent;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.v4.app.NavUtils;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.widget.EditText;
import android.widget.Toast;

import com.loopj.android.http.JsonHttpResponseHandler;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.UnsupportedEncodingException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

import cz.msebera.android.httpclient.Header;
import cz.msebera.android.httpclient.entity.StringEntity;
import cz.msebera.android.httpclient.message.BasicHeader;
import cz.msebera.android.httpclient.protocol.HTTP;

public class CreateMealActivity extends AppCompatActivity {

    private final String TAG = "CreateMealAcitivity";

    /**
     * Keep track of the login task to ensure we can cancel it if requested.
     */
    private CreateMealTask createMealTask = null;

    // UI references.
    private EditText nameView;
    private EditText decriptionView;
    private EditText priceView;
    private EditText expiryDateView;
    private EditText expiryTimeView;
    private EditText availableDateView;
    private EditText availableTimeView;
    private EditText servingsView;
    private EditText cusineView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_create_meal);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        getSupportActionBar().setDisplayHomeAsUpEnabled(true);

        // Set UI references
        nameView = (EditText) findViewById(R.id.name);
        decriptionView = (EditText) findViewById(R.id.description);
        priceView = (EditText) findViewById(R.id.price);
        expiryDateView = (EditText) findViewById(R.id.expiry_date);
        expiryTimeView = (EditText) findViewById(R.id.expiry_time);
        availableDateView = (EditText) findViewById(R.id.available_date);
        availableTimeView = (EditText) findViewById(R.id.available_time);
        servingsView = (EditText) findViewById(R.id.num_servings);
        cusineView = (EditText) findViewById(R.id.cusine);

    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.create_meal_menu, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle item selection
        switch (item.getItemId()) {

            case R.id.action_create_meal_cook:
                // Launch create meal screen
                attemptCreateMeal();
                return true;

            case R.id.action_create_meal_default:
                // Launch create meal screen
                loadDefaultMeal();
                return true;

            case R.id.action_create_meal_cancel:
                finish();
                return true;

            case android.R.id.home:
                NavUtils.navigateUpFromSameTask(this);
                return true;

            default:
                Toast.makeText(getBaseContext(), "Invalid option selected (but how?)", Toast.LENGTH_LONG).show();
                return super.onOptionsItemSelected(item);
        }
    }

    public void loadDefaultMeal(){
        nameView.setText("auto chicken meal");
        decriptionView.setText("This meal was auto generated");
        priceView.setText("11");
        expiryDateView.setText("2016-04-08");
        expiryTimeView.setText("15:00");
        availableDateView.setText("2016-04-10");
        availableTimeView.setText("18:30");
        servingsView.setText("4");
        cusineView.setText("Italian");
    }

    private void attemptCreateMeal(){
        Boolean cancel = false;
        SimpleDateFormat dateFormat = new SimpleDateFormat ("yyyy-MM-dd");
        SimpleDateFormat timeFormat = new SimpleDateFormat ("HH:mm");

        // Store values at the time of create meal attempt
        String name = nameView.getText().toString();
        String description = decriptionView.getText().toString();
        Double price = Double.parseDouble(priceView.getText().toString());
        Integer servings = Integer.parseInt(servingsView.getText().toString());
        String cusine = cusineView.getText().toString();

        Date expiryDate;
        Date expiryTime;
        Date availableDate;
        Date availableTime;

        try {
            expiryDate = dateFormat.parse(expiryDateView.getText().toString());
            expiryTime = timeFormat.parse(expiryTimeView.getText().toString());
            availableDate = dateFormat.parse(availableDateView.getText().toString());
            availableTime = timeFormat.parse(availableTimeView.getText().toString());
        } catch (ParseException e){
            Toast.makeText(getBaseContext(), "Invalid date or time", Toast.LENGTH_LONG).show();
            cancel = true;
            return;
        }

        //Add information to json object (must be in exact form) TODO: Add userid (must have it!), also check to see if user is logged in!
        JSONObject data = new JSONObject();

        try {
            data.put("meal_cook", ((AppInfo) getApplication()).getUserId());
            data.put("meal_name", name);
            data.put("meal_description", description);
            data.put("meal_available_date", dateFormat.format(availableDate));
            data.put("meal_available_time", timeFormat.format(availableTime));
            data.put("meal_expiry_date", dateFormat.format(expiryDate));
            data.put("meal_expiry_time", expiryTime);
            data.put("meal_price", price);
            data.put("meal_servings", servings);
            data.put("meal_cusine", cusine);
        } catch (JSONException e){
            Toast.makeText(getBaseContext(), "Invalid data (when converting to JSON object)", Toast.LENGTH_LONG).show();
        }

        //Execute meal create task
        if (cancel){
            Toast.makeText(getBaseContext(), "Meal create cancelled.", Toast.LENGTH_LONG).show();
        }
        else{
            createMealTask = new CreateMealTask(data);
            createMealTask.execute((Void) null);
        }
    }

    /**
     * Represents an asynchronous login/registration task used to authenticate
     * the user.
     */
    public class CreateMealTask extends AsyncTask<Void, Void, Boolean> {
        private JSONObject data;
        private int failStatusCode;
        Boolean successfullyCreated = false;

        CreateMealTask(JSONObject data) {
            this.data = data;
        }

        public void createMeal() {
            String url = "meals.json";

            StringEntity entity = null;
            try {
                entity = new StringEntity(data.toString());
                entity.setContentType(new BasicHeader(HTTP.CONTENT_TYPE, "application/json"));
            } catch (UnsupportedEncodingException e) {
                Log.e(TAG, "Invalid data. Could not parse to string. " + e.toString());
            }

            HomecookRESTApiClient homecookRestApi = ((AppInfo) getApplication()).homecookRestApi;

            homecookRestApi.sync_post_json(getBaseContext(), url, entity,
                    new JsonHttpResponseHandler() {

                        @Override
                        public void onSuccess(int statusCode, Header[] headers, JSONObject response) {
                            //Parse response to see if login successful and set isLoggedIn to True
                            Log.i(TAG, response.toString());
                            successfullyCreated = true;
                        }

                        @Override
                        public void onFailure(int statusCode, Header[] headers, Throwable throwable, JSONObject errorResponse) {
                            failStatusCode = statusCode;
                            Log.e(TAG, "Could not create meal (Status " + Integer.toString(statusCode) + "). errorResponse " + errorResponse.toString(), throwable);
                            successfullyCreated = false;
                        }

                        @Override
                        public void onFailure(int statusCode, Header[] headers, String message, Throwable throwable){
                            failStatusCode = statusCode;
                            Log.e(TAG, "Could not create meal (Status " + Integer.toString(statusCode) + ")", throwable);
                            successfullyCreated = false;
                        }
                    }
            );
        }

        @Override
        protected Boolean doInBackground(Void... params) {

            if(android.os.Debug.isDebuggerConnected())
                android.os.Debug.waitForDebugger();

            // Sets the isLoggedIn to true in AppInfo
            createMeal();
            return successfullyCreated;
        }

        @Override
        protected void onPostExecute(final Boolean success) {
            //Return value of doInBackground() is accessed and processed here.

            createMealTask = null;
            //showProgress(false);

            if (success) {
                String welcome_string = "Successfully created meal, " + ((AppInfo) getApplication()).getUserName() + "!";
                Toast.makeText(getBaseContext(), welcome_string, Toast.LENGTH_LONG).show();

                // create an Intent to take you over to a new DetailActivity
                Intent mainIntent = new Intent(getBaseContext(), MainActivity.class);
                startActivity(mainIntent);
                finish();
            }
            else {
                String error_string = "Create meal failed. (Status " + Integer.toString(failStatusCode) + ")";
                Toast.makeText(getBaseContext(), error_string, Toast.LENGTH_LONG).show();
            }
        }

        @Override
        protected void onCancelled() {
            createMealTask = null;
            //showProgress(false);
        }
    }
}
