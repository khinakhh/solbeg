<template>
    <div class="container">
      <div class="row">
        <div class="col-12">
          <table class="table table-bordered">
            <thead>
              <tr>
                <th scope="col">Id</th>
                <th scope="col">Name</th>
                <th scope="col">Description</th>
                <th scope="col">Country</th>
                <th scope="col">Actions</th>
              </tr>
            </thead>
            <tbody v-if="companies && companies.length">
              <tr v-for="company of companies" v-bind:key="company.id">
                <td>{{ company.id }}</td>
                <td>{{ company.name }}</td>
                <td>{{ company.description }}</td>
                <td>{{ company.country }}</td>
                <td class="td-actions">
                    <router-link :to="{name: 'company-edit', params: { id: company.id }}" class="btn btn-success"><i class="fas fa-edit"></i></router-link>
                    <button class="btn btn-danger" v-on:click="deleteCompany(company)"><i class="far fa-trash-alt"></i></button>
                </td>
              </tr>
            </tbody>
          </table>
          <div class="block-add">
            <router-link :to="{name: 'company-create'}" class="btn btn-primary rounded-0 btn-block">Create new company</router-link>
          </div>
          <p  v-if="companies.length == 0">No companies</p>
        </div>
      </div>
    </div>
</template>


<script>
import axios from 'axios';

export default {
    data() {
        return {
            companies: []
        }
    },
    created() {
        this.all();
    },
    methods: {
        all: function () {
            axios.get('http://127.0.0.1:8000/api/companies/')
                .then( response => {
                    this.companies = response.data
                    console.log("this.companies", this.companies)
                });
        },
        deleteCompany: function(company) {
            if (confirm('Delete ' + company.name)) {
                axios.delete(`http://127.0.0.1:8000/api/companies/${company.id}/`)
                    .then( response => {
                        this.all();
                    });
            }
        },
    },
}
</script>

<style>
.container {
  padding: 2rem 0rem;
}

h4 {
  margin: 2rem 0rem 1rem;
}

td, th {
  vertical-align: middle;
}

td.td-actions {
  border: 0;
}

.td-actions {
  display: flex;
  flex-direction: row;
  justify-content: center;
}

.btn-block {
  display: block;
  width: 20%;
}

.block-add {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
}
</style>