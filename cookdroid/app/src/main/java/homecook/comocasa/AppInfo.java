package homecook.comocasa;

import android.app.Application;
import android.content.SharedPreferences;
import android.preference.PreferenceActivity;
import android.util.Log;
import android.widget.Toast;

import org.json.*;
import com.loopj.android.http.*;

import org.json.JSONException;
import org.json.JSONObject;
import org.json.JSONArray;

import cz.msebera.android.httpclient.Header;

/**
 * Created by krishan on 16-03-09.
 * Implemnt AyncTask (to carry out setting the userId, etc in the background when logging in)
 */
public class AppInfo extends Application
{
    private static final String TAG = "AppInfo";

    //Some RESTAPI urls
    private static final String MEALS_URL = "http://127.0.0.1:8000/meals.json";
    private static final String USERS_URL = "http://127.0.0.1:8000/users.json";
    private static final String COOK_MEALS_URL = "http://127.0.0.1:8000/cook.meals/";

    //Store the userId for application-wide use
    private int userId;
    private Boolean isLoggedIn = false;

    //Save username and password for easy access
    private static final String PREFS = "prefs";
    private static final String PREF_USERID = "userid";
    private static final String PREF_EMAIL = "email";
    private static final String PREF_PASSWORD = "password";
    private static final String PREF_AUTOLOGIN = "autologin";
    private SharedPreferences mSharedPreferences;

    public AppInfo()
    {

    }

    public boolean Initialize()
    {
        //Initializing the app from shared preferences file

        // Read the user's name,
        // or an empty string if nothing found
        Integer userId = mSharedPreferences.getInt(PREF_USERID, 0);

        if (userId == 0) {
            // Not logged in...time to go do this
            Toast.makeText(this, "Not logged in, time to login pal...", Toast.LENGTH_LONG).show();
            loginSuccess = false;
            return false;
        }
        else
        {
            // If the name is valid. OK!
            Toast.makeText(this, "Welcome back " + userId.toString(), Toast.LENGTH_LONG).show();
            this.userId = userId;
            loginSuccess = true;
            return true;
        }
    }

    public Integer fetchUserId(String email)
    {
        //TODO: fetches the user_id from the given email for user

        Integer userId = 0;
        //Fetches the userId from API given the user's email

        return userId;
    }

    public void Initialize(String email, String password, boolean saveInfo)
    {
        //Initializing the app from login page
        mSharedPreferences = getSharedPreferences(PREFS, MODE_PRIVATE);
        // Get and set userId
        this.userId = fetchUserId(email);
        loginSuccess = true;

        if (saveInfo)
        {
            SharedPreferences.Editor e = mSharedPreferences.edit();
            e.putString(PREF_EMAIL, email);
            e.putString(PREF_PASSWORD, password);
            e.putBoolean(PREF_AUTOLOGIN, true);
            e.putInt(PREF_USERID, this.userId);
        }

        queryUsers();
    }

    public int getUserId(){
        return userId;
    }

    public boolean isLoggedIn()
    {
        return isLoggedIn;
    }

    private void queryUsers() {
        //Sample query for users utilizing RESTAPI

        // Prepare your search string to be put in a URL
        // It might have reserved characters or something
        //String urlString = "http://openlibrary.org/search.json?q=hunger+games+suzanne+collins";
        String urlString = "http://openlibrary.org/search.json?q=hunger+games+suzanne+collins";

        HomecookRestClientUsage.getMeals();
    }
}

class HomecookRestClientUsage {

    private static final String TAG = "HomecookRestClientUsage";

    public static void getMeals() {
        /*
        Handles meal data for meal view
         */

        HomecookRestClient.get("meals.json", null, new JsonHttpResponseHandler() {

            @Override
            public void onSuccess(int statusCode, Header[] headers, JSONObject response) {
                Log.d(TAG, response.toString());
                // If the response is JSONObject instead of expected JSONArray
            }

            @Override
            public void onSuccess(int statusCode, Header[] headers, JSONArray response) {
                Log.d(TAG, response.toString());
            }

            public void onFailure(int statusCode, Header[] headers, Throwable throwable, JSONObject errorResponse) {
                Log.d(TAG, "onFailure(int, Header[], Throwable, JSONObject) was not overriden, but callback was received", throwable);
            }

        });
    }
}
