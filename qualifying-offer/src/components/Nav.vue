<template>
  <b-navbar>
    <template #end>
      <b-navbar-item tag="div">
        <div class="buttons">
          <a class="button is-primary" @click="createData()">
            <strong>Load Data</strong>
          </a>
        </div>
      </b-navbar-item>
    </template>
  </b-navbar>
</template>

<script>
import axios from "axios";

export default {
  name: "Nav",
  data() {
    return {
      payArray: []
    };
  },
  methods: {
    async createData() {
      this.$store.commit("setDataLoading", true);
      await this.loadData();
      this.$store.commit("setPayArray", this.payArray);
      this.$store.commit("setDataLoading", false);
    },
    async loadData() {
      const res = await axios.get(
        "https://cors-anywhere.herokuapp.com/https://questionnaire-148920.appspot.com/swe/data.html"
      );
      let currentIndex = 0;

      do {
        currentIndex = res.data.indexOf("player-salary", currentIndex + 1);
        this.payArray.push(
          res.data.substring(
            res.data.indexOf(">", currentIndex + 1) + 1,
            res.data.indexOf("<", currentIndex + 1)
          )
        );
      } while (res.data.indexOf("player-salary", currentIndex + 1) !== -1);
    }
  }
};
</script>
