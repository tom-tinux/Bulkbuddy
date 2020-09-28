package comb.example.tom.myapplication;

import android.provider.MediaStore;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {


    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void checkButton(View v) {
        RadioGroup radio_activity = (RadioGroup) findViewById(R.id.radio_activity);
        final int checked_activity = radio_activity.getCheckedRadioButtonId();

        final RadioButton maleRadioButton = (RadioButton) findViewById(R.id.radio_male);
        final RadioButton femaleRadioButton = (RadioButton) findViewById(R.id.radio_female);

        Button calc_button = (Button) findViewById(R.id.calc_button);
        calc_button.setOnClickListener(new View.OnClickListener() {
            public void onClick(View view) {
                EditText height_input = (EditText) findViewById(R.id.height_input);
                EditText weight_input = (EditText) findViewById(R.id.weight_input);
                EditText age_input = (EditText) findViewById(R.id.age_input);
                TextView BMI_textview = (TextView) findViewById(R.id.BMI_textview);
                TextView BMR_textview = (TextView) findViewById(R.id.BMR_textview);
                TextView TDEE_textview = (TextView) findViewById(R.id.TDEE_textview);

                int height = Integer.parseInt(height_input.getText().toString());
                int weight = Integer.parseInt(weight_input.getText().toString());
                int age = Integer.parseInt(age_input.getText().toString());
                int BMI_result = (100 * 100 * weight) / (height * height);
                BMI_textview.setText("Your BMI is: " + BMI_result);

                if (maleRadioButton.isChecked()) {
                    String BMR_result = String.valueOf(((66.5 + (13.75 * weight)) + (5.003 * height) - (6.755 * age)));
                    int BMR_Integer = (int) ((66.5 + (13.75 * weight)) + (5.003 * height) - (6.755 * age));
                    BMR_textview.setText("Your BMR is: " + BMR_result);
                    int intvalue = (int) findViewById(checked_activity).getTag();
                    String TDEE_CALC = String.valueOf((BMR_Integer * intvalue));
                    TDEE_textview.setText("Your TDEE is: " + TDEE_CALC);
                }
                if (femaleRadioButton.isChecked()) {
                    String BMR_result = String.valueOf(((655.1 + (9.563 * weight)) + (1.850 * height) - (4.676 * age)));
                    BMR_textview.setText("Your BMR is: " + BMR_result);
                    String intvalue = findViewById(checked_activity).getTag().toString();
                    TDEE_textview.setText("Your TDEE is: " + intvalue);
                }
            }
        });
    }
}


