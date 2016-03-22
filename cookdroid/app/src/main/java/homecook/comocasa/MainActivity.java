package homecook.comocasa;

import android.content.Intent;
import android.os.Bundle;
import android.app.Activity;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.Window;
import android.widget.Button;
import android.widget.ListView;
import android.widget.Toast;

import com.loopj.android.http.JsonHttpResponseHandler;

import org.json.JSONArray;
import org.json.JSONObject;

import cz.msebera.android.httpclient.Header;

public class MainActivity extends AppCompatActivity {
    private static final String TAG = "MainActivity";

    ListView mealListView;
    JSONAdapter mJSONAdapter;
    JSONArray mealList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //Toolbar consists of all actions
        Toolbar myToolbar = (Toolbar) findViewById(R.id.main_toolbar);
        setSupportActionBar(myToolbar);     //set myToolbar as the ActionBar for the activity

        mJSONAdapter = new JSONAdapter(this, getLayoutInflater());
        mealListView = (ListView) findViewById(R.id.meal_listview);
        mealListView.setAdapter(mJSONAdapter);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.main_menu, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle item selection
        switch (item.getItemId()) {

            case R.id.action_create_meal:
                // Launch create meal screen
                Intent create_meal_intent = new Intent(getBaseContext(), CreateMealActivity.class);
                startActivity(create_meal_intent);
                return true;

            case R.id.action_refresh_meals:
                Toast.makeText(getBaseContext(), "Refreshing meals", Toast.LENGTH_LONG).show();
                refreshMeals();
                return true;

            case R.id.action_logout:
                Toast.makeText(getBaseContext(), "Loggin out...", Toast.LENGTH_LONG).show();
                // create an Intent to take you over to a new DetailActivity
                ((AppInfo) getApplication()).logOut();
                // Show login screen
                Intent login_intent = new Intent(getBaseContext(), LoginActivity.class);
                startActivity(login_intent);
                finish();
                return true;

            case R.id.action_settings:
                Toast.makeText(getBaseContext(), "Settings coming soon...", Toast.LENGTH_LONG).show();
                return true;

            default:
                Toast.makeText(getBaseContext(), "Invalid option selected (but how?)", Toast.LENGTH_LONG).show();
                return super.onOptionsItemSelected(item);
        }
    }

    private void refreshMeals(){
        //Get meals
        setProgressBarIndeterminateVisibility(true);

        String url = "meals/?format=json";
        HomecookRESTApiClient homecookRestApi = ((AppInfo) getApplication()).homecookRestApi;
        homecookRestApi.get(url, null,
                new JsonHttpResponseHandler() {

                    @Override
                    public void onSuccess(int statusCode, Header[] headers, JSONObject response) {
                        //Parse response to see if login successful and set isLoggedIn to True
                        Log.i(TAG, response.toString());
                    }

                    @Override
                    public void onSuccess(int statusCode, Header[] headers, JSONArray mealInfo) {
                        //Parse response to see if login successful and set isLoggedIn to True
                        Log.i(TAG, mealInfo.toString());
                        mealList = mealInfo;
                        mJSONAdapter.updateData(mealList);
                    }

                    @Override
                    public void onFailure(int statusCode, Header[] headers, Throwable throwable, JSONObject errorResponse) {
                        Log.e(TAG, "Could not get meals (Status " + Integer.toString(statusCode) + ")", throwable);
                    }

                }
        );

    }


}
