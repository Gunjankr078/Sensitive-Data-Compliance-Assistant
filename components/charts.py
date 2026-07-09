import streamlit as st
import plotly.express as px


def render_chart(detected_data):
    """
    Render sensitive data distribution pie chart.
    """

    st.subheader("📊 Sensitive Data Distribution")

    chart_data = {
        "Category": [],
        "Count": []
    }

    for category, matches in detected_data.items():

        chart_data["Category"].append(category)
        chart_data["Count"].append(len(matches))

    if sum(chart_data["Count"]) > 0:

        fig = px.pie(
            chart_data,
            names="Category",
            values="Count",
            hole=0.55,
            color_discrete_sequence=[
              "#4F46E5",
              "#7C3AED",
              "#60A5FA",
              "#10B981",
              "#F59E0B",
              "#EF4444",
              "#EC4899",
            ]
        )

        fig.update_layout(
            height=350,
            margin=dict(
                l=20,
                r=20,
                t=40,
                b=20
            ),
            legend_title="Sensitive Data"
        )

        fig.update_traces(
            textinfo="percent+label",
            pull=[0.03] * len(chart_data["Category"]),
            marker=dict(
            line=dict(color="white", width=2)
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            key="sensitive_data_distribution_chart"
        )

    else:

        st.info("No sensitive data detected.")