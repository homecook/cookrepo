package homecook.comocasa;

/**
 * Created by krishan on 16-03-11.
 */

import android.content.Context;
import com.loopj.android.http.*;
import cz.msebera.android.httpclient.entity.StringEntity;

public class HomecookRESTApiClient {

    // private static final String BASE_URL = "http://10.0.2.2:8000/";    //TODO: modify with the new server
    private static final String BASE_URL = "http://krisuj.pythonanywhere.com/";
    private AsyncHttpClient client = new AsyncHttpClient();
    private SyncHttpClient sync_client = new SyncHttpClient();

    public void set_auth(String username, String pass){
        client.setBasicAuth(username, pass);
        sync_client.setBasicAuth(username, pass);
    }

    private static String getJsonUrl(String url){
        return url + ".json";
    }

    private static String getAbsoluteUrl(String relativeUrl) {
        return BASE_URL + relativeUrl;
    }

    /*
    Asynchronous http client
     */
    public void get(String url, RequestParams params, AsyncHttpResponseHandler responseHandler) {
        client.get(getAbsoluteUrl(url), params, responseHandler);
    }

    public void post(String url, RequestParams params, AsyncHttpResponseHandler responseHandler) {
        client.post(getAbsoluteUrl(url), params, responseHandler);
    }

    public void post_json(Context context, String url, StringEntity entity, AsyncHttpResponseHandler responseHandler) {
        client.post(context, getAbsoluteUrl(url), entity, "application/json", responseHandler);
    }

    /*
    Synchronous http client
     */
    public void sync_get(String url, RequestParams params, AsyncHttpResponseHandler responseHandler) {
        sync_client.get(getAbsoluteUrl(url), params, responseHandler);
    }

    public void sync_post(String url, RequestParams params, AsyncHttpResponseHandler responseHandler) {
        sync_client.post(getAbsoluteUrl(url), params, responseHandler);
    }

    public void sync_post_json(Context context, String url, StringEntity entity, AsyncHttpResponseHandler responseHandler) {
        sync_client.post(context, getAbsoluteUrl(url), entity, "application/json", responseHandler);
    }
}