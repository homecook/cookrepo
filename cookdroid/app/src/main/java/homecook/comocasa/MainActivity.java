package homecook.comocasa;

import android.os.Bundle;
import android.app.Activity;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.view.View;
import android.view.Window;
import android.widget.Button;
import android.widget.ListView;

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
        Toolbar myToolbar = (Toolbar) findViewById(R.id.my_toolbar);
        setSupportActionBar(myToolbar);

        mJSONAdapter = new JSONAdapter(this, getLayoutInflater());
        mealListView = (ListView) findViewById(R.id.meal_listview);
        mealListView.setAdapter(mJSONAdapter);

        Button refreshMealsButton = (Button) findViewById(R.id.refresh_meals_button);
        refreshMealsButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                refreshMeals();
            }
        });     // on Click lauch attemptLogin function
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
