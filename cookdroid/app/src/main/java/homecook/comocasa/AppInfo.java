package homecook.comocasa;

import android.app.Application;
import android.content.SharedPreferences;
import android.util.Log;
import android.widget.Toast;

import com.loopj.android.http.*;

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

    public HomecookRESTApiClient homecookRestApi;

    public AppInfo()
    {
        homecookRestApi = new HomecookRESTApiClient();
    }

    public Integer fetchUserId(String email)
    {
        //TODO: fetches the user_id from the given email for user

        Integer userId = 0;
        //Fetches the userId from API given the user's email

        return userId;
    }

    //Initializing app instance (set userid, etc) from shared preferences file
    public boolean Initialize()
    {
        // Read the user's name,
        // or an empty string if nothing found
        Integer userId = mSharedPreferences.getInt(PREF_USERID, 0);

        if (userId == 0) {
            // Not logged in...time to go do this
            Toast.makeText(this, "Not logged in, time to login pal...", Toast.LENGTH_LONG).show();
            isLoggedIn = false;
            return false;
        }
        else
        {
            // If the name is valid. OK!
            Toast.makeText(this, "Welcome back " + userId.toString(), Toast.LENGTH_LONG).show();
            this.userId = userId;
            isLoggedIn = true;
            return true;
        }
    }

    //Initializing app instance (set userid, etc) from login page
    public void Initialize(String email, String password, boolean saveInfo)
    {
        mSharedPreferences = getSharedPreferences(PREFS, MODE_PRIVATE);
        // Get and set userId
        this.userId = fetchUserId(email);
        isLoggedIn = true;

        if (saveInfo)
        {
            SharedPreferences.Editor e = mSharedPreferences.edit();
            e.putString(PREF_EMAIL, email);
            e.putString(PREF_PASSWORD, password);
            e.putBoolean(PREF_AUTOLOGIN, true);
            e.putInt(PREF_USERID, this.userId);
        }

        HomecookRESTApiClientUsage.getMeals(homecookRestApi);
    }

    public int getUserId(){
        return userId;
    }

    //TODO: convert this to isLogged in property with get/set
    public boolean isLoggedIn()
    {
        return isLoggedIn;
    }

    public void setLogin(boolean success)
    {
        isLoggedIn = success;
    }

}

/**
 * Define all android interactions with the homecook API (maybe not the right way to do it...)
 */
class HomecookRESTApiClientUsage {

    private static final String TAG = "HomecookRestClientUsage";

    public static void getMeals(HomecookRESTApiClient homecookRestApi) {
        /*
        Handles meal data for meal view
         */

        homecookRestApi.get("meals.json", null, new JsonHttpResponseHandler() {

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
