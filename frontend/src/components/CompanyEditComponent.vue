<template>
    <div class="pt-5">
        <form @submit.prevent="update" method="post">
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
            <button type="submit" class="btn btn-primary">Update</button>
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
    mounted() {
        axios.get('http://127.0.0.1:8000/api/companies/' + this.$route.params.id + '/')
            .then( response => {
                console.log(response.data)
                this.company = response.data
            });
    },
    methods: {
        update: function (e) {
            this.$validator.validate().then(result => {
                this.submitted = true;
                if (!result) {
                    return;
                }
                axios
                    .put(`http://127.0.0.1:8000/api/companies/${this.company.id}/`,
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