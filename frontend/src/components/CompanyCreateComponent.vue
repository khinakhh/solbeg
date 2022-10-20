<template>
    <div class="pt-5">
        <form @submit.prevent="create" method="post">
            <div class="form-group">
                <label for="name">Name</label>
                <input
                    type="text"
                    class="form-control"
                    id="name"
                    v-model="company.name"
                    v-validate="'required'"
                    name="name"
                    placeholder="Enter name"
                >
            </div>

            <div class="form-group">
                <label for="description">Description</label>
                <input
                    type="text"
                    class="form-control"
                    id="description"
                    v-model="company.description"
                    v-validate="'required'"
                    name="description"
                    placeholder="Enter description"
                >
            </div>

            <div class="form-group">
                <label for="country">Country</label>
                <select
                    name="country"
                    class="form-control"
                    v-validate="'required'"
                    id="country"
                    v-model="company.country"
                >
                    <option value="BY">Belarus</option>
                    <option value="PL">Poland</option>
                    <option value="LT">Lithuania</option>
                    <option value="LV">Latvia</option>
                </select>
            </div>
            <button type="submit" class="btn btn-primary">Create</button>
        </form>
    </div>
</template>

<script>

import axios from 'axios';

export default {
    data() {
        return {
            company: {
                name: '',
                description: '',
                country: '',
            },
            submitted: false
        }
    },
    methods: {
        create: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios
                    .post('http://127.0.0.1:8000/api/companies/',
                        this.company
                    )
                    .then(response => {
                        this.$router.push('/companies');
                    })
            });
        }
    },
}
</script>