package homecook.comocasa;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONObject;

/**
 * Created by krishan on 16-03-15.
 */
public class JSONAdapter extends BaseAdapter {

    Context mContext;
    LayoutInflater mInflater;
    JSONArray mJsonArray;

    public JSONAdapter (Context context, LayoutInflater inflater) {
        mContext = context;
        mInflater = inflater;
        mJsonArray = new JSONArray();
    }

    @Override
    public int getCount() {
        return mJsonArray.length();
    }

    @Override
    public Object getItem(int position) {
        return mJsonArray.optJSONObject(position);
    }

    @Override
    public long getItemId(int position) {
        return position;    //Does not do anything for us..
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        ViewHolder holder;

        // check if the view already exists
        // if so, no need to inflate and findViewById again!
        if (convertView == null) {

            // Inflate the custom row layout from your XML.
            convertView = mInflater.inflate(R.layout.row_meal, null);

            // create a new "Holder" with subviews
            holder = new ViewHolder();
            holder.thumbnailImageView = (ImageView) convertView.findViewById(R.id.img_thumbnail);
            holder.nameTextView = (TextView) convertView.findViewById(R.id.name);
            holder.cookTextView = (TextView) convertView.findViewById(R.id.cook);

            // hang onto this holder for future recyclage
            convertView.setTag(holder);
        } else {

            // skip all the expensive inflation/findViewById
            // and just get the holder you already made
            holder = (ViewHolder) convertView.getTag();
        }

        // Set data
        //--------------------------------------------------------

        JSONObject jsonObject = (JSONObject) getItem(position);

        //Set image to default
        holder.thumbnailImageView.setImageResource(R.drawable.ic_arrow_forward_black_24dp);

        // Grab meal name and cook if it can be parsed from json object
        String name = "unknown";
        String cook = "unknown";

        if (jsonObject.has("meal_name")) {
            name = jsonObject.optString("meal_name");
        }

        if (jsonObject.has("meal_cook")) {
            cook = jsonObject.optString("meal_cook");
        }

        // Send these Strings to the TextViews for display
        holder.nameTextView.setText(name);
        holder.cookTextView.setText(cook);

        return convertView;
    }

    public void updateData(JSONArray jsonArray) {
        // update the adapter's dataset
        mJsonArray = jsonArray;
        notifyDataSetChanged();     //this is a method borrowed from the BaseAdapter class
    }

    // this is used so you only ever have to do inflation and finding by ID once ever per View
    private static class ViewHolder {
        public ImageView thumbnailImageView;
        public TextView nameTextView;
        public TextView cookTextView;
    }

}