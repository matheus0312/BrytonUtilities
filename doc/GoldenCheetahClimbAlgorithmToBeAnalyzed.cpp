    // FIND ASCENTS
    if (methodClimb->isChecked()) {

        // Verifies if data is long enough and contains altitude data
        if (ride->areDataPresent()->alt == false || ride->dataPoints().count() < 3) return;

        double hysteresis = appsettings->value(NULL, GC_ELEVATION_HYSTERESIS).toDouble();
        if (hysteresis <= 0.1) hysteresis = 3.00;

        // first apply hysteresis
        QVector<QPoint> points; 

        int index=0;
        int runningAlt = ride->dataPoints().first()->alt;

        foreach(RideFilePoint *p, ride->dataPoints()) {

            // up
            if (p->alt > (runningAlt + hysteresis)) {
                runningAlt = p->alt;
                points << QPoint(index, runningAlt);
            }

            // down
            if (p->alt < (runningAlt - hysteresis)) {
                runningAlt = p->alt;
                points << QPoint(index, runningAlt);
            }
            index++;
        }

        // now find peaks and troughs in the point data
        // there will only be ups and downs, no flats
        QVector<QPoint> peaks;
        for(int i=1; i<(points.count()-1); i++) {

            // peak
            if (points[i].y() > points[i-1].y() &&
                points[i].y() > points[i+1].y()) peaks << points[i];

            // trough
            if (points[i].y() < points[i-1].y() &&
                points[i].y() < points[i+1].y()) peaks << points[i];
        }

        // now run through looking for diffs > requested
        int counter=0;
        for (int i=0; i<(peaks.count()-1); i++) {

            int ascent = 0; // ascent found in meters
            if ((ascent=peaks[i+1].y() - peaks[i].y()) >= altSpinBox->value()) {

                // found one so increment from zero
                counter++;

                // we have a winner...
                struct AddedInterval add;
                add.start = ride->dataPoints()[peaks[i].x()]->secs;
                add.stop = ride->dataPoints()[peaks[i+1].x()]->secs;
                add.name = QString(tr("Climb #%1 (%2m)")).arg(counter)
                                                        .arg(ascent);
                results << add;

            }
        }
    }
