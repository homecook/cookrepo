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
 * Maintains the state of the application
 */
public class AppInfo extends Application
{
    private static final String TAG = "AppInfo";

    //Store the userId for application-wide use
    private String userId;
    private String password;
    private Boolean isLoggedIn = false;

    //Save username and password for easy access
    private static final String PREFS = "prefs";
    private static final String PREF_USERID = "userid";
    private static final String PREF_EMAIL = "email";
    private static final String PREF_PASSWORD = "password";
    private static final String PREF_AUTOLOGIN = "autologin";
    private SharedPreferences mSharedPreferences;

    // The homecook REST web api instance that is used throughout the application
    public HomecookRESTApiClient homecookRestApi;

    public AppInfo()
    {
        homecookRestApi = new HomecookRESTApiClient();
    }

    //Initializing app instance (set userid, etc) from shared preferences file
    //TODO: Must update this to make sure all information can is validated against the server
    public boolean Initialize()
    {
        // Read the user's name,
        // or an empty string if nothing found
        String userId = mSharedPreferences.getString(PREF_USERID, "");

        if (userId == "") {
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
    public void Initialize(String email, String username, String password, boolean saveInfo)
    {
        mSharedPreferences = getSharedPreferences(PREFS, MODE_PRIVATE);
        // Get and set userId
        this.userId = username;
        this.password = password;
        isLoggedIn = true;

        if (saveInfo)
        {
            SharedPreferences.Editor e = mSharedPreferences.edit();
            e.putString(PREF_EMAIL, email);
            e.putString(PREF_PASSWORD, password);
            e.putBoolean(PREF_AUTOLOGIN, true);
            e.putString(PREF_USERID, username);
        }

        //TODO: Authenticate homecookRestApi by providing username/password
        Log.i(TAG, "Successfully initialized app-info, and logged in " + username);

    }

    //TODO: convert this to isLogged in property with get/set
    public boolean isLoggedIn() {
        return isLoggedIn;
    }

    public String getUserId(){
        return userId;
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
