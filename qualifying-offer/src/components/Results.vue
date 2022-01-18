<template>
  <section class="section">
    <div class="card" v-if="payArray.length === 0">
      <div class="card-content">
        <div class="content">
          Please click on the load data button to begin.
        </div>
      </div>
    </div>
    <div class="card" v-else>
      <div class="card-content">
        <div class="content">
          <p>Next year's qualifying offer is {{ this.qualifyingOffer }}.</p>
          <p>The average salary last season was {{ averagePayLastSeason }}.</p>
          <p>The highest paid salary last season was {{ highestPaid }}.</p>
          <p>The lowest paid salary last season was {{ lowestPaid }}.</p>
          <p>
            There were {{ this.payArray.length - this.filtered.length }} blank
            or data points removed.
          </p>
        </div>
      </div>
    </div>

    <b-loading
      :is-full-page="false"
      v-model="isLoading"
      :can-cancel="true"
    ></b-loading>
  </section>
</template>

<script>
export default {
  name: "results",
  computed: {
    payArray() {
      return this.$store.state.payArray;
    },
    isLoading() {
      return this.$store.state.dataLoading;
    }
  },
  data() {
    return {
      filtered: [],
      qualifyingOffer: 0,
      averagePayLastSeason: 0,
      highestPaid: 0,
      lowestPaid: 0
    };
  },
  watch: {
    payArray: function(newArray) {
      let topSum = 0;
      let totalSum = 0;
      // Grabbed this from https://stackoverflow.com/questions/149055/how-to-format-numbers-as-currency-strings
      const formatter = new Intl.NumberFormat("en-US", {
        style: "currency",
        currency: "USD"
      });

      this.filtered = newArray.filter((salary) => salary.includes("$"));
      this.filtered.forEach((salary, index) => {
        let newValue = Number(salary.replace(/[\\$\\,]/g, ""));
        totalSum += newValue;
        this.filtered[index] = newValue;
      });
      let sorted = this.filtered;
      sorted.sort((a, b) => b - a);
      this.highestPaid = formatter.format(sorted[0]);
      this.lowestPaid = formatter.format(sorted[sorted.length - 1]);

      sorted.slice(0, 125).forEach((val) => (topSum += val));

      this.qualifyingOffer = formatter.format(topSum / 125);
      this.averagePayLastSeason = formatter.format(
        totalSum / this.filtered.length
      );
    }
  }
};
</script>

<style></style>
